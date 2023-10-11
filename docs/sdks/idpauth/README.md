# IDPAuth
(*idp_auth*)

### Available Operations

* [get](#get) - Get IDP used for an authorization code callback

## get

Get IDP used for an authorization code callback

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.idp_auth.get(code='female', state='program')

if res.success is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `code`             | *Optional[str]*    | :heavy_minus_sign: | Authorization Code |
| `state`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetIDPAuthResponse](../../models/operations/getidpauthresponse.md)**

