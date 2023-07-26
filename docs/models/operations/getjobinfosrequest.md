# GetJobInfosRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `collector_id`                                                | *Optional[str]*                                               | :heavy_minus_sign:                                            | Filter by collector id, e.g. "collectorId=Prometheus-in"      |
| `id`                                                          | *Optional[str]*                                               | :heavy_minus_sign:                                            | Filter by job id, e.g. "id=1608713335.3&id=1608713326.1"      |
| `limit`                                                       | *Optional[int]*                                               | :heavy_minus_sign:                                            | Maximum number of items to return                             |
| `offset`                                                      | *Optional[int]*                                               | :heavy_minus_sign:                                            | Pagination offset                                             |
| `run_type`                                                    | *Optional[str]*                                               | :heavy_minus_sign:                                            | Filter by job run type, one of "adhoc", "scheduled", "system" |
| `state`                                                       | *Optional[str]*                                               | :heavy_minus_sign:                                            | Filter by current job state, e.g. "running"                   |