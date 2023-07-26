# sample_content

### Available Operations

* [get](#get) - Get sample content by ID

## get

Get sample content by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSampleContentRequest(
    id='80809437-3e06-4045-9beb-bad02f2586bc',
)

res = s.sample_content.get(req)

if res.sample_contents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetSampleContentRequest](../../models/operations/getsamplecontentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetSampleContentResponse](../../models/operations/getsamplecontentresponse.md)**

