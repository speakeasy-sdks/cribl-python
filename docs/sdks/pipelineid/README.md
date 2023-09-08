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


res = s.pipeline_id.delete(id='rerum')

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


res = s.pipeline_id.get(id='eos')

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


res = s.pipeline_id.update(id='reprehenderit', pipeline=shared.Pipeline(
    conf=shared.PipelineConf(
        async_func_timeout=345506,
        description='neque',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='iusto',
                disabled=False,
                filter='est',
                final=False,
                group_id='rem',
                id='cd9e7319-c177-4d52-9f77-b114eeb52ff7',
            ),
        ],
        groups={
            "praesentium": shared.PipelineConfGroups(
                description='nemo',
                disabled=False,
                name='Devin Donnelly',
            ),
        },
        output='illo',
        streamtags=[
            'labore',
        ],
    ),
    id='d4c98e0c-2bb8-49eb-b5da-d636c600503d',
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

