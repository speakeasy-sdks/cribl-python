# DataSample
(*data_sample*)

### Available Operations

* [post](#post) - Create DataSample

## post

Create DataSample

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.DataSample(
    additional_properties={
        "payment": 'Silver',
    },
    id='<ID>',
    sample_name='iste',
)

res = s.data_sample.post(req)

if res.data_samples is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.DataSample](../../models/shared/datasample.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.PostDataSampleResponse](../../models/operations/postdatasampleresponse.md)**

