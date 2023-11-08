# ListDataSample
(*.list_data_sample*)

### Available Operations

* [get](#get) - Get a list of DataSample objects

## get

Get a list of DataSample objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.list_data_sample.get()

if res.data_samples is not None:
    # handle response
    pass
```


### Response

**[operations.GetListDataSampleResponse](../../models/operations/getlistdatasampleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
