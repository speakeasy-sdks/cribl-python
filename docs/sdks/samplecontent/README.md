# SampleContent
(*.sample_content*)

### Available Operations

* [get](#get) - Get sample content by ID

## get

Get sample content by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.sample_content.get(id='string')

if res.sample_contents is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Sample ID          |


### Response

**[operations.GetSampleContentResponse](../../models/operations/getsamplecontentresponse.md)**

