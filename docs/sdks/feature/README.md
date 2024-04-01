# Feature
(*feature*)

### Available Operations

* [get](#get) - Get feature by Id

## get

Get feature by id (i.e. 'type/name`)

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.feature.get(id='<value>')

if res.features_entry is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Feature id         |


### Response

**[operations.GetFeatureResponse](../../models/operations/getfeatureresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
