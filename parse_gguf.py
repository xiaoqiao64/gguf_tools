#!/Users/rainforest/envs/base/.venv/bin/python
"""Parse a GGUF file and print model metadata + tensor types.

Basic info tables follow gguf-parser-go (METADATA / ARCHITECTURE / TOKENIZER).
"""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter
from typing import Any

from gguf import (
    GGUFEndian,
    GGUFReader,
    Keys,
    LlamaFileType,
    model_weight_count_rounded_notation,
)

NA = "N/A"


def kv(reader: GGUFReader, key: str, default: Any = None) -> Any:
    field = reader.get_field(key)
    if field is None:
        return default
    return field.contents()


def kv_arch(reader: GGUFReader, template: str, arch: str, default: Any = None) -> Any:
    return kv(reader, template.format(arch=arch), default)


def fmt_bytes(n: float) -> str:
    for unit, scale in (("TiB", 1024**4), ("GiB", 1024**3), ("MiB", 1024**2), ("KiB", 1024)):
        if n >= scale:
            return f"{n / scale:.2f} {unit}"
    return f"{int(n)} B"


def fmt_quant(file_type: Any) -> str:
    if file_type is None:
        return NA
    try:
        name = LlamaFileType(int(file_type)).name
    except ValueError:
        return str(file_type)
    if name.startswith("MOSTLY_"):
        name = name[len("MOSTLY_") :]
    return name


def fmt_val(val: Any) -> str:
    if val is None:
        return NA
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, list):
        if not val:
            return NA
        if len(val) == 1:
            return str(val[0])
        shown = val[:8]
        text = ", ".join(str(x) for x in shown)
        if len(val) > 8:
            text += ", ..."
        return f"[{text}]"
    return str(val)


def md_cell(val: str) -> str:
    return val.replace("|", "\\|").replace("\n", " ")


def print_table(title: str, headers: list[str], rows: list[list[str]]) -> None:
    print(f"## {title}\n")
    print("| " + " | ".join(md_cell(h) for h in headers) + " |")
    print("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        print("| " + " | ".join(md_cell(c) for c in row) + " |")
    print()


def dump_metadata(reader: GGUFReader, path: str) -> None:
    arch = kv(reader, Keys.General.ARCHITECTURE, NA)
    model_type = kv(reader, Keys.General.TYPE, "model")
    name = kv(reader, Keys.General.NAME) or os.path.basename(path)
    little_endian = reader.endianess == GGUFEndian.LITTLE

    n_params = sum(t.n_elements for t in reader.tensors)
    n_bytes = sum(t.n_bytes for t in reader.tensors)
    bpw = (n_bytes * 8 / n_params) if n_params else 0.0

    file_size = os.path.getsize(path)
    version = kv(reader, "GGUF.version")
    tensor_count = kv(reader, "GGUF.tensor_count")
    kv_count = kv(reader, "GGUF.kv_count")

    print_table(
        "METADATA",
        ["TYPE", "NAME", "ARCH", "QUANTIZATION", "LITTLE ENDIAN", "SIZE", "PARAMETERS", "BPW"],
        [[
            fmt_val(model_type),
            fmt_val(name),
            fmt_val(arch),
            fmt_quant(kv(reader, Keys.General.FILE_TYPE)),
            "true" if little_endian else "false",
            fmt_bytes(n_bytes),
            f"{model_weight_count_rounded_notation(n_params)}" if n_params else NA,
            f"{bpw:.2f} bpw" if n_params else NA,
        ]],
    )
    print(f"- file: `{path}`")
    print(f"- gguf version: {fmt_val(version)}")
    print(f"- file size: {fmt_bytes(file_size)}")
    print(f"- tensors: {fmt_val(tensor_count)}")
    print(f"- kv: {fmt_val(kv_count)}")
    print()

    if arch == NA:
        return

    vocab = kv_arch(reader, Keys.LLM.VOCAB_SIZE, arch)
    tokens_field = reader.get_field(Keys.Tokenizer.LIST)
    if vocab is None and tokens_field is not None:
        vocab = len(tokens_field.data)

    print_table(
        "ARCHITECTURE",
        [
            "MAX CONTEXT LEN",
            "EMBEDDING LEN",
            "ATTENTION CAUSAL",
            "ATTENTION HEAD CNT",
            "LAYERS",
            "FEED FORWARD LEN",
            "EXPERT CNT",
            "VOCABULARY LEN",
        ],
        [[
            fmt_val(kv_arch(reader, Keys.LLM.CONTEXT_LENGTH, arch)),
            fmt_val(kv_arch(reader, Keys.LLM.EMBEDDING_LENGTH, arch)),
            fmt_val(kv_arch(reader, Keys.Attention.CAUSAL, arch)),
            fmt_val(kv_arch(reader, Keys.Attention.HEAD_COUNT, arch)),
            fmt_val(kv_arch(reader, Keys.LLM.BLOCK_COUNT, arch)),
            fmt_val(kv_arch(reader, Keys.LLM.FEED_FORWARD_LENGTH, arch)),
            fmt_val(kv_arch(reader, Keys.LLM.EXPERT_COUNT, arch)),
            fmt_val(vocab),
        ]],
    )


def dump_tokenizer(reader: GGUFReader) -> None:
    tokens_field = reader.get_field(Keys.Tokenizer.LIST)
    if tokens_field is None and kv(reader, Keys.Tokenizer.MODEL) is None:
        return

    tokens_len = len(tokens_field.data) if tokens_field is not None else None
    tokens_size = (
        sum(int(p.nbytes) for p in tokens_field.parts) if tokens_field is not None else None
    )

    print_table(
        "TOKENIZER",
        [
            "MODEL",
            "TOKENS SIZE",
            "TOKENS LEN",
            "BOS TOKEN",
            "EOS TOKEN",
            "EOT TOKEN",
            "EOM TOKEN",
            "UNKNOWN TOKEN",
            "SEPARATOR TOKEN",
            "PADDING TOKEN",
        ],
        [[
            fmt_val(kv(reader, Keys.Tokenizer.MODEL)),
            fmt_bytes(tokens_size) if tokens_size is not None else NA,
            fmt_val(tokens_len),
            fmt_val(kv(reader, Keys.Tokenizer.BOS_ID)),
            fmt_val(kv(reader, Keys.Tokenizer.EOS_ID)),
            fmt_val(kv(reader, Keys.Tokenizer.EOT_ID)),
            fmt_val(kv(reader, Keys.Tokenizer.EOM_ID)),
            fmt_val(kv(reader, Keys.Tokenizer.UNK_ID)),
            fmt_val(kv(reader, Keys.Tokenizer.SEP_ID)),
            fmt_val(kv(reader, Keys.Tokenizer.PAD_ID)),
        ]],
    )


def dump_tensors(reader: GGUFReader) -> None:
    rows = [
        [str(i), tensor.name, tensor.tensor_type.name]
        for i, tensor in enumerate(reader.tensors)
    ]
    print_table("TENSORS", ["#", "NAME", "TENSOR_TYPE"], rows)

    counts = Counter(t.tensor_type.name for t in reader.tensors)
    summary = ", ".join(f"`{name}`={n}" for name, n in counts.most_common())
    print(f"**tensor type counts:** {summary}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse GGUF model metadata and tensor types")
    parser.add_argument("-m", "--model", required=True, help="Path to .gguf model file")
    args = parser.parse_args()

    path = args.model
    if not os.path.isfile(path):
        print(f"error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    reader = GGUFReader(path, "r")
    dump_metadata(reader, path)
    dump_tokenizer(reader)
    dump_tensors(reader)


if __name__ == "__main__":
    main()
