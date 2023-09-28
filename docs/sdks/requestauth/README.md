# RequestAuth
(*request_auth*)

### Available Operations

* [get](#get) - Accepts an authentication request from an IDP and authenticates the user
* [post](#post) - API call that the IDP should use for an authentication request

## get

Accepts an authentication request from an IDP and authenticates the user

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.request_auth.get(relay_state='quaerat', saml_response='blanditiis')

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `relay_state`                 | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `saml_response`               | *Optional[str]*               | :heavy_minus_sign:            | Authentication request object |


### Response

**[operations.GetRequestAuthResponse](../../models/operations/getrequestauthresponse.md)**


## post

API call that the IDP should use for an authentication request

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostRequestAuthRequestBody(
    relay_state='distinctio',
    saml_response='nisi',
)

res = s.request_auth.post(req)

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostRequestAuthRequestBody](../../models/operations/postrequestauthrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PostRequestAuthResponse](../../models/operations/postrequestauthresponse.md)**

