# pipeline_id

### Available Operations

* [delete](#delete) - Delete Pipeline
* [get](#get) - Get Pipeline by ID
* [update](#update) - Update Pipeline

## delete

Delete Pipeline

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeletePipelineIDRequest(
    id='41ff5d4e-2ae4-4fb5-8b35-d17638f1edb7',
)

res = s.pipeline_id.delete(req)

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeletePipelineIDRequest](../../models/operations/deletepipelineidrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeletePipelineIDResponse](../../models/operations/deletepipelineidresponse.md)**


## get

Get Pipeline by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetPipelineIDRequest(
    id='8359ecc5-cb86-40f8-8d58-0ba73810e4fe',
)

res = s.pipeline_id.get(req)

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetPipelineIDRequest](../../models/operations/getpipelineidrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetPipelineIDResponse](../../models/operations/getpipelineidresponse.md)**


## update

Update Pipeline

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdatePipelineIDRequest(
    pipeline=shared.Pipeline(
        conf=shared.PipelineConf(
            async_func_timeout=269889,
            description='quaerat',
            functions=[
                shared.PipelineFunctionConf(
                    conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                    description='voluptate',
                    disabled=False,
                    filter='magni',
                    final=False,
                    group_id='excepturi',
                    id='7cd3b1dd-3bbc-4e24-bb76-84eff50126d7',
                ),
                shared.PipelineFunctionConf(
                    conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                    description='veritatis',
                    disabled=False,
                    filter='nobis',
                    final=False,
                    group_id='voluptatibus',
                    id='fbd0eb74-b842-4195-bb44-bd3c43159d33',
                ),
            ],
            groups={
                "veniam": shared.PipelineConfGroups(
                    description='provident',
                    disabled=False,
                    name='Mr. Carmen Schmidt Jr.',
                ),
                "amet": shared.PipelineConfGroups(
                    description='occaecati',
                    disabled=False,
                    name='Gilbert Dickinson',
                ),
                "modi": shared.PipelineConfGroups(
                    description='et',
                    disabled=False,
                    name='Gene Rowe DDS',
                ),
                "porro": shared.PipelineConfGroups(
                    description='explicabo',
                    disabled=False,
                    name='Willie Weissnat',
                ),
            },
            output='ullam',
            streamtags=[
                'quisquam',
            ],
        ),
        id='9a41ffbe-9cbd-4795-ae65-e076cc7abf61',
    ),
    id='6ea5c716-4193-44b9-8f2e-09d19d2fc2f9',
)

res = s.pipeline_id.update(req)

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdatePipelineIDRequest](../../models/operations/updatepipelineidrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdatePipelineIDResponse](../../models/operations/updatepipelineidresponse.md)**

