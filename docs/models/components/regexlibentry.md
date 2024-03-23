# RegexLibEntry


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `id`                                              | *str*                                             | :heavy_check_mark:                                | N/A                                               |
| `regex`                                           | *str*                                             | :heavy_check_mark:                                | Regex pattern. Required.                          |
| `description`                                     | *Optional[str]*                                   | :heavy_minus_sign:                                | Brief description of this regex. Optional.        |
| `lib`                                             | *Optional[str]*                                   | :heavy_minus_sign:                                | N/A                                               |
| `sample_data`                                     | *Optional[str]*                                   | :heavy_minus_sign:                                | Sample data for this regex. Optional.             |
| `tags`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | One or more tags related to this regex. Optional. |