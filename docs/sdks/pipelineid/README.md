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
    bearer_auth="",
)


res = s.pipeline_id.delete(id='string')

if res.pipelines is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.pipeline_id.get(id='string')

if res.pipelines is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.pipeline_id.update(id='string', pipeline=shared.Pipeline(
    conf=shared.PipelineConf(
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                id='<ID>',
            ),
        ],
        groups={
            "key": shared.PipelineConfGroups(
                name='string',
            ),
        },
        streamtags=[
            'string',
        ],
    ),
    id='<ID>',
))

if res.pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique ID                                                    |
| `pipeline`                                                   | [Optional[shared.Pipeline]](../../models/shared/pipeline.md) | :heavy_minus_sign:                                           | Pipeline object to be updated                                |


### Response

**[operations.UpdatePipelineIDResponse](../../models/operations/updatepipelineidresponse.md)**

