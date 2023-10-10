# CreatePipeline
(*create_pipeline*)

### Available Operations

* [post](#post) - Create Pipeline

## post

Create Pipeline

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.Pipeline(
    conf={
        "payment": 'Silver',
    },
    id='<ID>',
)

res = s.create_pipeline.post(req)

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [shared.Pipeline](../../models/shared/pipeline.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.PostCreatePipelineResponse](../../models/operations/postcreatepipelineresponse.md)**

