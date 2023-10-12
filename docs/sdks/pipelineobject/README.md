# PipelineObject
(*pipeline_object*)

### Available Operations

* [get](#get) - Get a list of Pipeline objects

## get

Get a list of Pipeline objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.pipeline_object.get()

if res.pipelines is not None:
    # handle response
```


### Response

**[operations.GetPipelineObjectResponse](../../models/operations/getpipelineobjectresponse.md)**

