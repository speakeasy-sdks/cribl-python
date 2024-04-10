# Container
(*container*)

### Available Operations

* [get](#get) - Get details for a single container on the edge host. Add stream=true to get a stream instead.

## get

Get details for a single container on the edge host. Add stream=true to get a stream instead.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.container.get(id='<value>')

if res.containers is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetContainerResponse](../../models/operations/getcontainerresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
