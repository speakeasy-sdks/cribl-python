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

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.request_auth.get(relay_state='<value>', saml_response='<value>')

if res.success is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `relay_state`                 | *Optional[str]*               | :heavy_minus_sign:            | N/A                           |
| `saml_response`               | *Optional[str]*               | :heavy_minus_sign:            | Authentication request object |


### Response

**[operations.GetRequestAuthResponse](../../models/operations/getrequestauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400,401,429      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## post

API call that the IDP should use for an authentication request

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.PostRequestAuthRequestBody()

res = s.request_auth.post(req)

if res.success is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostRequestAuthRequestBody](../../models/operations/postrequestauthrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PostRequestAuthResponse](../../models/operations/postrequestauthresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 400,401,429      | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
