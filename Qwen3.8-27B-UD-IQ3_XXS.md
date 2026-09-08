## METADATA


| TYPE  | NAME        | ARCH   | QUANTIZATION | LITTLE ENDIAN | SIZE      | PARAMETERS | BPW      |
| ----- | ----------- | ------ | ------------ | ------------- | --------- | ---------- | -------- |
| model | Qwen3.8-27B | qwen35 | IQ3_XXS      | true          | 10.17 GiB | 27B        | 3.20 bpw |


- file: `~/gguf/Qwen3.8-27B-UD-IQ3_XXS.gguf`
- gguf version: 3
- file size: 10.18 GiB
- tensors: 866
- kv: 50

## ARCHITECTURE


| MAX CONTEXT LEN | EMBEDDING LEN | ATTENTION CAUSAL | ATTENTION HEAD CNT | LAYERS | FEED FORWARD LEN | EXPERT CNT | VOCABULARY LEN |
| --------------- | ------------- | ---------------- | ------------------ | ------ | ---------------- | ---------- | -------------- |
| 262144          | 5120          | N/A              | 24                 | 65     | 17408            | N/A        | 248320         |




## TOKENIZER


| MODEL | TOKENS SIZE | TOKENS LEN | BOS TOKEN | EOS TOKEN | EOT TOKEN | EOM TOKEN | UNKNOWN TOKEN | SEPARATOR TOKEN | PADDING TOKEN |
| ----- | ----------- | ---------- | --------- | --------- | --------- | --------- | ------------- | --------------- | ------------- |
| gpt2  | 4.63 MiB    | 248320     | 248044    | 248046    | N/A       | N/A       | N/A           | N/A             | 248055        |




## TENSORS


| #   | NAME                                                                                             | TENSOR_TYPE | COUNT |
| --- | ------------------------------------------------------------------------------------------------ | ----------- | ----- |
| 0   | output.weight                                                                                    | Q4_K        | 1     |
| 1   | output_norm.weight                                                                               | F32         | 1     |
| 2   | token_embd.weight                                                                                | Q2_K        | 1     |
| 3   | blk.0.attn_gate.weight                                                                           | IQ4_XS      | 1     |
| 4   | blk.064.attn_norm.weight                                                                         | F32         | 65    |
| 5   | blk.0.attn_qkv.weight                                                                            | IQ4_XS      | 1     |
| 6   | blk.0,910,16.ffn_down.weight                                                                     | IQ2_XS      | 4     |
| 7   | blk.0,15,17.ffn_gate.weight                                                                      | IQ1_S       | 3     |
| 8   | blk.0,1214.ffn_up.weight                                                                         | IQ1_S       | 4     |
| 9   | blk.064.post_attention_norm.weight                                                               | F32         | 65    |
| 10  | blk.02,46,810,1214,1618,2022,2426,2830,3234,3638,4042,4446,4850,5254,5658,6062.ssm_a             | F32         | 48    |
| 11  | blk.02,46,810,1214,1618,2022,2426,2830,3234,3638,4042,4446,4850,5254,5658,6062.ssm_alpha.weight  | Q8_0        | 48    |
| 12  | blk.02,46,810,1214,1618,2022,2426,2830,3234,3638,4042,4446,4850,5254,5658,6062.ssm_beta.weight   | Q8_0        | 48    |
| 13  | blk.02,46,810,1214,1618,2022,2426,2830,3234,3638,4042,4446,4850,5254,5658,6062.ssm_conv1d.weight | F32         | 48    |
| 14  | blk.02,46,810,1214,1618,2022,2426,2830,3234,3638,4042,4446,4850,5254,5658,6062.ssm_dt.bias       | F32         | 48    |
| 15  | blk.02,46,810,1214,1618,2022,2426,2830,3234,3638,4042,4446,4850,5254,5658,6062.ssm_norm.weight   | F32         | 48    |
| 16  | blk.01.ssm_out.weight                                                                            | Q4_K        | 2     |
| 17  | blk.12,6,8,12,20,22,26,3234,3638,4042,44,46,50,5254,62.attn_gate.weight                          | IQ3_XXS     | 24    |
| 18  | blk.1,4,38.attn_qkv.weight                                                                       | IQ2_S       | 3     |
| 19  | blk.1,3,21,26,2830,32,4248.ffn_down.weight                                                       | IQ3_XXS     | 15    |
| 20  | blk.1,11,14,16,18.ffn_gate.weight                                                                | IQ2_XXS     | 5     |
| 21  | blk.1,911,1517,19.ffn_up.weight                                                                  | IQ2_XXS     | 8     |
| 22  | blk.2,56,10,17,2122,2425,30,3637,4042,44,50,5254,57.attn_qkv.weight                              | IQ3_XXS     | 21    |
| 23  | blk.2,20,2223,25,27,3441,4953,62.ffn_down.weight                                                 | IQ3_S       | 20    |
| 24  | blk.28,3133,35,46.ffn_gate.weight                                                                | IQ2_S       | 12    |
| 25  | blk.24,78,29.ffn_up.weight                                                                       | IQ2_S       | 6     |
| 26  | blk.2,5,25,50,5253,5658,60,62.ssm_out.weight                                                     | IQ4_XS      | 11    |
| 27  | blk.3,19,31,35,43,47,51,55,59,63.attn_k.weight                                                   | Q4_K        | 10    |
| 28  | blk.3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,6364.attn_k_norm.weight                           | F32         | 17    |
| 29  | blk.3,43.attn_output.weight                                                                      | Q4_K        | 2     |
| 30  | blk.3,7,11,15.attn_q.weight                                                                      | Q2_K        | 4     |
| 31  | blk.3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,6364.attn_q_norm.weight                           | F32         | 17    |
| 32  | blk.3,7,11,15,19,39,43,47,55.attn_v.weight                                                       | Q4_K        | 9     |
| 33  | blk.45,21,2425,2830,5658,6061.attn_gate.weight                                                   | IQ3_S       | 13    |
| 34  | blk.46,1819,31,33.ffn_down.weight                                                                | IQ2_S       | 7     |
| 35  | blk.4,6,9,2022,26,28,30,3234,3637,4042,44,46,4849,54,61.ssm_out.weight                           | IQ3_S       | 23    |
| 36  | blk.5,2324,28,3037,4448,50.ffn_up.weight                                                         | IQ3_XXS     | 18    |
| 37  | blk.6,18.ffn_up.weight                                                                           | IQ2_XS      | 2     |
| 38  | blk.7,11,15,23,39.attn_k.weight                                                                  | IQ3_S       | 5     |
| 39  | blk.7,11.attn_output.weight                                                                      | IQ3_XXS     | 2     |
| 40  | blk.7.ffn_down.weight                                                                            | Q2_K        | 1     |
| 41  | blk.89,1213.attn_qkv.weight                                                                      | IQ2_XXS     | 4     |
| 42  | blk.8,1112,17.ffn_down.weight                                                                    | IQ2_XXS     | 4     |
| 43  | blk.8,10,17.ssm_out.weight                                                                       | Q3_K        | 3     |
| 44  | blk.910,13,16,45,48.attn_gate.weight                                                             | IQ2_S       | 6     |
| 45  | blk.910,12,19,30.ffn_gate.weight                                                                 | IQ2_XS      | 5     |
| 46  | blk.1214,18,24,29,38,45.ssm_out.weight                                                           | IQ3_XXS     | 8     |
| 47  | blk.13.ffn_down.weight                                                                           | IQ1_S       | 1     |
| 48  | blk.13.ffn_gate.weight                                                                           | IQ1_M       | 1     |
| 49  | blk.14.attn_gate.weight                                                                          | IQ2_XXS     | 1     |
| 50  | blk.14,18.attn_qkv.weight                                                                        | Q2_K        | 2     |
| 51  | blk.1415.ffn_down.weight                                                                         | IQ1_M       | 2     |
| 52  | blk.15.attn_output.weight                                                                        | IQ2_XXS     | 1     |
| 53  | blk.16,20,26,2829,3234,4546,4849,56,58,6062.attn_qkv.weight                                      | IQ3_S       | 17    |
| 54  | blk.16.ssm_out.weight                                                                            | IQ2_S       | 1     |
| 55  | blk.17.attn_gate.weight                                                                          | IQ2_XS      | 1     |
| 56  | blk.18,49.attn_gate.weight                                                                       | Q2_K        | 2     |
| 57  | blk.19,23,47.attn_output.weight                                                                  | IQ3_S       | 3     |
| 58  | blk.19.attn_q.weight                                                                             | IQ2_XXS     | 1     |
| 59  | blk.2024,2729,34,3640,4245,4753,55.ffn_gate.weight                                               | IQ3_XXS     | 26    |
| 60  | blk.20,22,2627,3843,49,5155.ffn_up.weight                                                        | IQ3_S       | 16    |
| 61  | blk.21,25.ffn_up.weight                                                                          | Q3_K        | 2     |
| 62  | blk.23,27,43,51.attn_q.weight                                                                    | IQ3_S       | 4     |
| 63  | blk.23,27,31,35,51,59,63.attn_v.weight                                                           | Q5_K        | 7     |
| 64  | blk.24.ffn_down.weight                                                                           | Q3_K        | 1     |
| 65  | blk.2526,41,54,56.ffn_gate.weight                                                                | IQ3_S       | 5     |
| 66  | blk.27.attn_k.weight                                                                             | IQ4_XS      | 1     |
| 67  | blk.27,31,35,39,51,55,59,63.attn_output.weight                                                   | IQ4_XS      | 8     |
| 68  | blk.31,35,39,47,55,59.attn_q.weight                                                              | IQ3_XXS     | 6     |
| 69  | blk.5461.ffn_down.weight                                                                         | IQ4_XS      | 8     |
| 70  | blk.5662.ffn_up.weight                                                                           | IQ4_XS      | 7     |
| 71  | blk.5763.ffn_gate.weight                                                                         | IQ4_XS      | 7     |
| 72  | blk.63.attn_q.weight                                                                             | IQ4_XS      | 1     |
| 73  | blk.63.ffn_down.weight                                                                           | Q4_K        | 1     |
| 74  | blk.63.ffn_up.weight                                                                             | Q4_K        | 1     |
| 75  | blk.64.attn_k.weight                                                                             | Q8_0        | 1     |
| 76  | blk.64.attn_output.weight                                                                        | Q6_K        | 1     |
| 77  | blk.64.attn_q.weight                                                                             | Q6_K        | 1     |
| 78  | blk.64.attn_v.weight                                                                             | Q8_0        | 1     |
| 79  | blk.64.ffn_down.weight                                                                           | Q6_K        | 1     |
| 80  | blk.64.ffn_gate.weight                                                                           | Q6_K        | 1     |
| 81  | blk.64.ffn_up.weight                                                                             | Q6_K        | 1     |
| 82  | blk.64.nextn.eh_proj.weight                                                                      | Q6_K        | 1     |
| 83  | blk.64.nextn.enorm.weight                                                                        | F32         | 1     |
| 84  | blk.64.nextn.hnorm.weight                                                                        | F32         | 1     |
| 85  | blk.64.nextn.shared_head_norm.weight                                                             | F32         | 1     |


**tensor type counts:** `F32`=360, `IQ3_XXS`=120, `IQ3_S`=106, `Q8_0`=98, `IQ4_XS`=45, `IQ2_S`=35, `Q4_K`=26, `IQ2_XXS`=24, `IQ2_XS`=12, `Q2_K`=10, `IQ1_S`=8, `Q5_K`=7, `Q3_K`=6, `Q6_K`=6, `IQ1_M`=3