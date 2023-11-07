# DataSample
(*.data_sample*)

### Available Operations

* [post](#post) - Create DataSample

## post

Create DataSample

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.DataSample(
    additional_properties={
        "key": 'string',
    },
    id='<ID>',
    sample_name='string',
)

res = s.data_sample.post(req)

if res.data_samples is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [components.DataSample](../../models/shared/datasample.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.PostDataSampleResponse](../../models/operations/postdatasampleresponse.md)**

