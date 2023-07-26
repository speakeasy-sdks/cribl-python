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
        async_func_timeout=885208,
        description='eos',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='odio',
                disabled=False,
                filter='praesentium',
                final=False,
                group_id='odit',
                id='259e3ea4-b519-47f9-a443-da7ce52b895c',
            ),
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='enim',
                disabled=False,
                filter='neque',
                final=False,
                group_id='in',
                id='c6454efb-0b34-4896-83ca-5acfbe2fd570',
            ),
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='odio',
                disabled=False,
                filter='minima',
                final=False,
                group_id='in',
                id='7929177d-eac6-446e-8b57-3409e3eb1e5a',
            ),
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='dolores',
                disabled=False,
                filter='nam',
                final=False,
                group_id='dicta',
                id='2eb07f11-6db9-4954-9fc9-5fa88970e189',
            ),
        ],
        groups={
            "tempore": shared.PipelineConfGroups(
                description='libero',
                disabled=False,
                name='Sharon Windler',
            ),
            "ipsum": shared.PipelineConfGroups(
                description='adipisci',
                disabled=False,
                name='Doug Baumbach',
            ),
            "libero": shared.PipelineConfGroups(
                description='architecto',
                disabled=False,
                name='Fernando Roob',
            ),
            "magnam": shared.PipelineConfGroups(
                description='itaque',
                disabled=False,
                name='Ollie Harris',
            ),
        },
        output='laudantium',
        streamtags=[
            'pariatur',
        ],
    ),
    id='3513bb6f-48b6-456b-8db3-5ff2e4b27537',
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

