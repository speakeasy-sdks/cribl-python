# EventBreakerID
(*.event_breaker_id*)

### Available Operations

* [get](#get) - Get Event Breaker Ruleset by ID

## get

Get Event Breaker Ruleset by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.event_breaker_id.get(id='string')

if res.event_breaker_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetEventBreakerIDResponse](../../models/operations/geteventbreakeridresponse.md)**

