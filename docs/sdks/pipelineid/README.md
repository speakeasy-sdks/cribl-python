# PipelineID
(*pipeline_id*)

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


res = s.pipeline_id.delete(id='program')

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.pipeline_id.get(id='female')

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.pipeline_id.update(id='Van', pipeline=shared.Pipeline(
    conf=shared.PipelineConf(
        async_func_timeout=15652,
        description='Future-proofed next generation workforce',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='Extended modular open architecture',
                disabled=False,
                filter='invoice Arizona',
                final=False,
                group_id='mostly',
                id='<ID>',
            ),
        ],
        groups={
            "in": shared.PipelineConfGroups(
                description='Horizontal dynamic productivity',
                disabled=False,
                name='bifurcated',
            ),
        },
        output='silver immediately',
        streamtags=[
            'implement',
        ],
    ),
    id='<ID>',
))

if res.pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique ID                                                    |
| `pipeline`                                                   | [Optional[shared.Pipeline]](../../models/shared/pipeline.md) | :heavy_minus_sign:                                           | Pipeline object to be updated                                |


### Response

**[operations.UpdatePipelineIDResponse](../../models/operations/updatepipelineidresponse.md)**

