# GetLogFileListRequest


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `allow`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | query array[string] optional List of allowed-filename wildcard patterns |
| `depth`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Search depth for "manual" mode                                          |
| `mode`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Discovery Mode (default is "auto")                                      |
| `path`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Search directory for "manual" mode                                      |