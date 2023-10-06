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
    conf=shared.PipelineConf(
        async_func_timeout=449035,
        description='Quality-focused non-volatile functionalities',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='Organic mobile strategy',
                disabled=False,
                filter='Metrics synergize',
                final=False,
                group_id='Direct Grenada',
                id='<ID>',
            ),
        ],
        groups={
            "sunt": shared.PipelineConfGroups(
                description='Object-based scalable process improvement',
                disabled=False,
                name='withdrawal',
            ),
        },
        output='intelligence',
        streamtags=[
            'array',
        ],
    ),
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

