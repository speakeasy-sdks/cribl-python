# sample_content

### Available Operations

* [get](#get) - Get sample content by ID

## get

Get sample content by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.sample_content.get(id='fuga')

if res.sample_contents is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Sample ID          |


### Response

**[operations.GetSampleContentResponse](../../models/operations/getsamplecontentresponse.md)**

