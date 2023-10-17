# Feature
(*feature*)

### Available Operations

* [get](#get) - Get feature by Id

## get

Get feature by id (i.e. 'type/name`)

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.feature.get(id='female')

if res.features_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Feature id         |


### Response

**[operations.GetFeatureResponse](../../models/operations/getfeatureresponse.md)**

