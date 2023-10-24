# InternalSystemMetrics
(*internal_system_metrics*)

### Available Operations

* [post](#post) - Aggregate raw internal system metrics

## post

Aggregate raw internal system metrics

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.MetricsAggOpts(
    aggs=shared.AggregationMgrOptions(
        aggregations=[
            'string',
        ],
        cumulative=False,
        flush_event_limit=449035,
        flush_mem_limit=690234,
        hostname='scared-godparent.name',
        metrics_mode=False,
        split_bys=[
            'string',
        ],
        sufficient_stats_only=False,
        time_window_seconds=614946,
    ),
    metrics=shared.MetricsStore(),
)

res = s.internal_system_metrics.post(req)

if res.metrics_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.MetricsAggOpts](../../models/shared/metricsaggopts.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostInternalSystemMetricsResponse](../../models/operations/postinternalsystemmetricsresponse.md)**

