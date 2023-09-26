# PipelineID

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


res = s.pipeline_id.delete(id='enim')

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


res = s.pipeline_id.get(id='hic')

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


res = s.pipeline_id.update(id='animi', pipeline=shared.Pipeline(
    conf=shared.PipelineConf(
        async_func_timeout=559774,
        description='totam',
        functions=[
            shared.PipelineFunctionConf(
                conf=shared.PipelineFunctionConfFunctionSpecificConfigs(),
                description='molestias',
                disabled=False,
                filter='odio',
                final=False,
                group_id='eaque',
                id='e189dbb3-0fcb-433e-a055-b197cd44e2f5',
            ),
        ],
        groups={
            "consequuntur": shared.PipelineConfGroups(
                description='facere',
                disabled=False,
                name='Fred Stracke',
            ),
        },
        output='ab',
        streamtags=[
            'velit',
        ],
    ),
    id='bb6f48b6-56bc-4db3-9ff2-e4b27537a8cd',
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

