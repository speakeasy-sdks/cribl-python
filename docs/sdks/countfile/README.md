# CountFile
(*count_file*)

### Available Operations

* [get](#get) - get the count of files of changed

## get

get the count of files of changed

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.count_file.get(group='<value>')

if res.count_file is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group`            | *Optional[str]*    | :heavy_minus_sign: | Group ID           |


### Response

**[operations.GetCountFileResponse](../../models/operations/getcountfileresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
