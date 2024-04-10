# InternalSystemMetrics
(*internal_system_metrics*)

### Available Operations

* [post](#post) - Aggregate raw internal system metrics

## post

Aggregate raw internal system metrics

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.MetricsAggOpts(
    aggs=components.AggregationMgrOptions(
        aggregations=[
            '<value>',
        ],
        cumulative=False,
        flush_event_limit=449035,
        flush_mem_limit=690234,
        hostname='scared-godparent.name',
        metrics_mode=False,
        sufficient_stats_only=False,
        time_window_seconds=614946,
    ),
)

res = s.internal_system_metrics.post(req)

if res.metrics_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.MetricsAggOpts](../../models/components/metricsaggopts.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostInternalSystemMetricsResponse](../../models/operations/postinternalsystemmetricsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
