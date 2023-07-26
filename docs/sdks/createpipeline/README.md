# create_pipeline

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
        async_func_timeout=959143,
        description='officiis',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='fuga',
                disabled=False,
                filter='pariatur',
                final=False,
                group_id='debitis',
                id='008e6f8c-5f35-40d8-8db5-a34181430104',
            ),
        ],
        groups={
            "ab": shared.PipelineConfGroups(
                description='laudantium',
                disabled=False,
                name='Rosa Stiedemann',
            ),
        },
        output='ipsa',
        streamtags=[
            'eveniet',
            'impedit',
            'officiis',
        ],
    ),
    id='7e253b66-8451-4c6c-ae20-5e16deab3fec',
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

