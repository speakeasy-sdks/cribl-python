# SendDiagBundle


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `include_metrics`                                                       | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Toggle to No to exclude metrics from the diag bundle.                   |
| `max_include_jobs`                                                      | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Number of jobs including all tasks that will be included in the bundle. |
| `path`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Existing diag bundle that will be send to Cribl Support. Max 100MB.     |
| `rename_js`                                                             | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Append .txt to JavaScript files.                                        |
| `send_to_cribl`                                                         | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Send diag bundle to Cribl Support                                       |