# internal_system_metrics

### Available Operations

* [post](#post) - Aggregate raw internal system metrics

## post

Aggregate raw internal system metrics

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.MetricsAggOpts(
    aggs=shared.AggregationMgrOptions(
        aggregations=[
            'alias',
        ],
        cumulative=False,
        flush_event_limit=910073,
        flush_mem_limit=941668,
        hostname='altruistic-doorpost.biz',
        idle_time_limit_seconds=185897,
        lag_tolerance_seconds=895912,
        metrics_mode=False,
        prefix='harum',
        preserve_split_by_structure=False,
        search_agg_mode='explicabo',
        split_bys=[
            'aliquid',
        ],
        sufficient_stats_only=False,
        time_window_seconds=264649,
    ),
    always_bounds=False,
    metrics=shared.MetricsStore(),
    where='optio',
)

res = s.internal_system_metrics.post(req)

if res.metrics_response is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.MetricsAggOpts](../../models/shared/metricsaggopts.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostInternalSystemMetricsResponse](../../models/operations/postinternalsystemmetricsresponse.md)**

