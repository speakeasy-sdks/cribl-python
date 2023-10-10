# AggregationMgrOptions


## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `aggregations`                | list[*str*]                   | :heavy_check_mark:            | N/A                           |
| `cumulative`                  | *Optional[bool]*              | :heavy_check_mark:            | N/A                           |
| `flush_event_limit`           | *Optional[int]*               | :heavy_check_mark:            | N/A                           |
| `flush_mem_limit`             | *Optional[int]*               | :heavy_check_mark:            | N/A                           |
| `hostname`                    | *Optional[str]*               | :heavy_check_mark:            | N/A                           |
| `idle_time_limit_seconds`     | *Optional[int]*               | :heavy_minus_sign:            | N/A                           |
| `lag_tolerance_seconds`       | *Optional[int]*               | :heavy_minus_sign:            | N/A                           |
| `metrics_mode`                | *Optional[bool]*              | :heavy_check_mark:            | N/A                           |
| `prefix`                      | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `preserve_split_by_structure` | *Optional[bool]*              | :heavy_minus_sign:            | N/A                           |
| `search_agg_mode`             | *Optional[Any]*               | :heavy_minus_sign:            | N/A                           |
| `split_bys`                   | list[*str*]                   | :heavy_minus_sign:            | N/A                           |
| `sufficient_stats_only`       | *Optional[bool]*              | :heavy_check_mark:            | N/A                           |
| `time_window_seconds`         | *Optional[int]*               | :heavy_check_mark:            | N/A                           |