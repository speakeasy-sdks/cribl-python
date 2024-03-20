# EventBreakerID
(*event_breaker_id*)

### Available Operations

* [get](#get) - Get Event Breaker Ruleset by ID

## get

Get Event Breaker Ruleset by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.event_breaker_id.get(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
