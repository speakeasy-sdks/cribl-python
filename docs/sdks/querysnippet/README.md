# QuerySnippet
(*query_snippet*)

### Available Operations

* [apply](#apply) - Applies a query snippet on a set of input events for preview

## apply

Applies a query snippet on a set of input events for preview

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.PreviewRequestBody(
    events=[
        'string',
    ],
    query='string',
)

res = s.query_snippet.apply(req)

if res.preview_responses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.PreviewRequestBody](../../models/components/previewrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ApplyQuerySnippetResponse](../../models/operations/applyquerysnippetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
