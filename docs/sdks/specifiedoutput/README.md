# SpecifiedOutput
(*specified_output*)

### Available Operations

* [get](#get) - Get samples data for the specified output. Used to get sample data for the test action.

## get

Get samples data for the specified output. Used to get sample data for the test action.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.specified_output.get(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.GetSpecifiedOutputResponse](../../models/operations/getspecifiedoutputresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
