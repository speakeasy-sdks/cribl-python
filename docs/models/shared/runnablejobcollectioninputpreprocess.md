# RunnableJobCollectionInputPreprocess


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `args`                                                                       | list[*str*]                                                                  | :heavy_minus_sign:                                                           | Arguments                                                                    |
| `command`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Command to feed the data through (via stdin) and process its output (stdout) |
| `disabled`                                                                   | *bool*                                                                       | :heavy_check_mark:                                                           | Enable Custom Command                                                        |