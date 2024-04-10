# ListEventBreaker
(*list_event_breaker*)

### Available Operations

* [get](#get) - Get a list of Event Breaker Ruleset objects

## get

Get a list of Event Breaker Ruleset objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_event_breaker.get()

if res.event_breaker_rulesets is not None:
    # handle response
    pass

```


### Response

**[operations.GetListEventBreakerResponse](../../models/operations/getlisteventbreakerresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
