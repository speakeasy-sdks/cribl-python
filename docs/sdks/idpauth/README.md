# IDPAuth
(*idp_auth*)

### Available Operations

* [get](#get) - Get IDP used for an authorization code callback

## get

Get IDP used for an authorization code callback

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `code`             | *Optional[str]*    | :heavy_minus_sign: | Authorization Code |
| `state`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetIDPAuthResponse](../../models/operations/getidpauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
