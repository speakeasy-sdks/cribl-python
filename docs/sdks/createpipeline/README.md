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
        async_func_timeout=231701,
        description='vero',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='tenetur',
                disabled=False,
                filter='dignissimos',
                final=False,
                group_id='hic',
                id='bc7abd74-dd39-4c0f-9d2c-ff7c70a45626',
            ),
        ],
        groups={
            "possimus": shared.PipelineConfGroups(
                description='magnam',
                disabled=False,
                name='Mrs. Vicki Langosh',
            ),
        },
        output='quasi',
        streamtags=[
            'ex',
        ],
    ),
    id='d9f5fce6-c556-4146-83e2-50fb008c42e1',
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

