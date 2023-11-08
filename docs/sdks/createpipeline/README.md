# CreatePipeline
(*.create_pipeline*)

### Available Operations

* [post](#post) - Create Pipeline

## post

Create Pipeline

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.Pipeline(
    conf=components.PipelineConf(
        functions=[
            components.PipelineFunctionConf(
                conf=components.FunctionSpecificConfigs(),
                id='<ID>',
            ),
        ],
        groups={
            "key": components.PipelineGroups(
                name='string',
            ),
        },
        streamtags=[
            'string',
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

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [components.Pipeline](../../models/shared/pipeline.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.PostCreatePipelineResponse](../../models/operations/postcreatepipelineresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
