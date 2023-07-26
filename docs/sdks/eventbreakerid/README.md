# event_breaker_id

### Available Operations

* [get](#get) - Get Event Breaker Ruleset by ID

## get

Get Event Breaker Ruleset by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetEventBreakerIDRequest(
    id='4ccca99b-c7fc-40b2-9ce1-0873e42b006d',
)

res = s.event_breaker_id.get(req)

if res.event_breaker_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetEventBreakerIDRequest](../../models/operations/geteventbreakeridrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetEventBreakerIDResponse](../../models/operations/geteventbreakeridresponse.md)**

