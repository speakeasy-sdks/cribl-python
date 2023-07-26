# request_auth

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

req = operations.GetRequestAuthRequest(
    relay_state='dicta',
    saml_response='molestiae',
)

res = s.request_auth.get(req)

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetRequestAuthRequest](../../models/operations/getrequestauthrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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
    relay_state='maxime',
    saml_response='dolores',
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

