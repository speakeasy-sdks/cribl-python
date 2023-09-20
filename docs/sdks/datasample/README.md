# DataSample

### Available Operations

* [post](#post) - Create DataSample

## post

Create DataSample

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = {
    "non": 'et',
}

res = s.data_sample.post(req)

if res.data_samples is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostDataSampleResponse](../../models/operations/postdatasampleresponse.md)**

