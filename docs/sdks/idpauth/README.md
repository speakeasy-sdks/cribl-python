# IDPAuth
(*idp_auth*)

### Available Operations

* [get](#get) - Get IDP used for an authorization code callback

## get

Get IDP used for an authorization code callback

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
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
| errors.SDKError  | 400-600          | */*              |
