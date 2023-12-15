# PipelineObject
(*pipeline_object*)

### Available Operations

* [get](#get) - Get a list of Pipeline objects

## get

Get a list of Pipeline objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.pipeline_object.get()

if res.pipelines is not None:
    # handle response
    pass
```


### Response

**[operations.GetPipelineObjectResponse](../../models/operations/getpipelineobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
