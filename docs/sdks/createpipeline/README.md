# CreatePipeline
(*create_pipeline*)

### Available Operations

* [post](#post) - Create Pipeline

## post

Create Pipeline

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.Pipeline(
    conf=components.PipelineConf(),
    id='<id>',
)

res = s.create_pipeline.post(req)

if res.pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [components.Pipeline](../../models/components/pipeline.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.PostCreatePipelineResponse](../../models/operations/postcreatepipelineresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
