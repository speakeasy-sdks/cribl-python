# search_job_metrics

### Available Operations

* [get](#get) - Get search job metrics

## get

Get search job metrics

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GethSearchJobMetricsRequest(
    id='849bf821-4c33-47f9-abb0-c69e372db134',
)

res = s.search_job_metrics.get(req)

if res.geth_search_job_metrics_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GethSearchJobMetricsRequest](../../models/operations/gethsearchjobmetricsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GethSearchJobMetricsResponse](../../models/operations/gethsearchjobmetricsresponse.md)**

