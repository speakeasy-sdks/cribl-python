# QuerySnippet
(*query_snippet*)

### Available Operations

* [apply](#apply) - Applies a query snippet on a set of input events for preview

## apply

Applies a query snippet on a set of input events for preview

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.PreviewRequestBody(
    events=[
        'interface',
    ],
    options=shared.PreviewOptions(),
    query='structure Aruba hourly',
)

res = s.query_snippet.apply(req)

if res.preview_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PreviewRequestBody](../../models/shared/previewrequestbody.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.ApplyQuerySnippetResponse](../../models/operations/applyquerysnippetresponse.md)**

