# SearchJobMetrics
(*search_job_metrics*)

### Available Operations

* [get](#get) - Get search job metrics

## get

Get search job metrics

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_job_metrics.get(id='<value>')

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.GethSearchJobMetricsResponse](../../models/operations/gethsearchjobmetricsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
