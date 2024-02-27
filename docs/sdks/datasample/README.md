# DataSample
(*data_sample*)

### Available Operations

* [post](#post) - Create DataSample

## post

Create DataSample

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.DataSample(
    id='<id>',
    sample_name='<value>',
)

res = s.data_sample.post(req)

if res.data_samples is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [components.DataSample](../../models/components/datasample.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostDataSampleResponse](../../models/operations/postdatasampleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
