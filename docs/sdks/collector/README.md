# Collector

### Available Operations

* [get](#get) - Get Collector by ID

## get

Get Collector by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.collector.get(id='provident')

if res.collectors is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetCollectorResponse](../../models/operations/getcollectorresponse.md)**

