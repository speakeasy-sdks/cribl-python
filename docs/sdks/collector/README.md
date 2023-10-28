# Collector
(*collector*)

### Available Operations

* [get](#get) - Get Collector by ID

## get

Get Collector by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.collector.get(id='string')

if res.collectors is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetCollectorResponse](../../models/operations/getcollectorresponse.md)**

