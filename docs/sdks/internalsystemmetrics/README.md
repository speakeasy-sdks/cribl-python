# InternalSystemMetrics

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
            'mollitia',
        ],
        cumulative=False,
        flush_event_limit=333965,
        flush_mem_limit=29100,
        hostname='splendid-track.com',
        idle_time_limit_seconds=542457,
        lag_tolerance_seconds=442036,
        metrics_mode=False,
        prefix='asperiores',
        preserve_split_by_structure=False,
        search_agg_mode='totam',
        split_bys=[
            'suscipit',
        ],
        sufficient_stats_only=False,
        time_window_seconds=693957,
    ),
    always_bounds=False,
    metrics=shared.MetricsStore(),
    where='maxime',
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

