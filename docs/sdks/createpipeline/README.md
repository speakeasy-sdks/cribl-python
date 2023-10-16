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
    bearer_auth="",
)

req = shared.Pipeline(
    conf=shared.PipelineConf(
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                id='<ID>',
            ),
        ],
        groups={
            "payment": shared.PipelineConfGroups(
                name='base mealy Metrics',
            ),
        },
        streamtags=[
            'synergize',
        ],
    ),
    id='<ID>',
)

res = s.create_pipeline.post(req)

if res.pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [shared.Pipeline](../../models/shared/pipeline.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.PostCreatePipelineResponse](../../models/operations/postcreatepipelineresponse.md)**

