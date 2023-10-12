# SearchJobMetrics
(*search_job_metrics*)

### Available Operations

* [get](#get) - Get search job metrics

## get

Get search job metrics

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.search_job_metrics.get(id='female')

if res.geth_search_job_metrics_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.GethSearchJobMetricsResponse](../../models/operations/gethsearchjobmetricsresponse.md)**

