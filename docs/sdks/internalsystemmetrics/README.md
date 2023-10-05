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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.MetricsAggOpts(
    aggs=shared.AggregationMgrOptions(
        aggregations=[
            'payment',
        ],
        cumulative=False,
        flush_event_limit=722100,
        flush_mem_limit=390366,
        hostname='needy-order.org',
        idle_time_limit_seconds=520911,
        lag_tolerance_seconds=42444,
        metrics_mode=False,
        prefix='Metrics synergize Arizona',
        preserve_split_by_structure=False,
        search_agg_mode='synthesizing',
        split_bys=[
            'withdrawal',
        ],
        sufficient_stats_only=False,
        time_window_seconds=15395,
    ),
    always_bounds=False,
    metrics=shared.MetricsStore(),
    where='Southeast array',
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

