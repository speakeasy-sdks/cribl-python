# EventBreakerOnData
(*event_breaker_on_data*)

### Available Operations

* [post](#post) - Runs an event breaker rule on the specified data

## post

Runs an event breaker rule on the specified data

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.DatatypePreviewRequestBody(
    input='<value>',
)

res = s.event_breaker_on_data.post(req)

if res.preview_responses is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.DatatypePreviewRequestBody](../../models/components/datatypepreviewrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PostEventBreakerOnDataResponse](../../models/operations/posteventbreakerondataresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
