# QueryMetricsRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `earliest`                                                                    | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | earliest time to query against                                                |
| `filter_expr`                                                                 | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | a js expression to apply against the metrics returned (can filter dimensions) |
| `latest`                                                                      | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | latest time to query against                                                  |
| `metric_name_filter`                                                          | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | can be a regex or an array of metric names                                    |
| `num_buckets`                                                                 | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | buckets in the past to include in the query results                           |