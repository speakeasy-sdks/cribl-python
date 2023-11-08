# One


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `description`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Brief description of this lookup. Optional.                      |
| `file_info`                                                      | [Optional[components.FileInfo]](../../models/shared/fileinfo.md) | :heavy_minus_sign:                                               | Uploaded file information                                        |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Filename with the lookup table. Required.                        |
| `size`                                                           | *Optional[int]*                                                  | :heavy_minus_sign:                                               | File size. Optional.                                             |
| `tags`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | One or more tags related to this lookup. Optional.               |