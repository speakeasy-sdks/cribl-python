# ScriptLibEntry


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `command`                                                | *str*                                                    | :heavy_check_mark:                                       | Command to execute for this script                       |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `additional_properties`                                  | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | N/A                                                      |
| `args`                                                   | List[*str*]                                              | :heavy_minus_sign:                                       | Arguments to pass when executing this script             |
| `description`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Brief description of this script. Optional.              |
| `env`                                                    | Dict[str, *str*]                                         | :heavy_minus_sign:                                       | Extra environment variables to set when executing script |