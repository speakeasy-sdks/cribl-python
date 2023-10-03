# GetBytesRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `path`                                                                             | *Optional[str]*                                                                    | :heavy_check_mark:                                                                 | The path to the file to sample                                                     |
| `bytes_requested`                                                                  | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | The number of bytes to return;   this value could be constrained by system limits. |