# EventBreaker
(*event_breaker*)

### Available Operations

* [delete](#delete) - Delete Event Breaker Ruleset
* [post](#post) - Create Event Breaker Ruleset
* [update](#update) - Update Event Breaker Ruleset

## delete

Delete Event Breaker Ruleset

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.event_breaker.delete(id='string')

if res.event_breaker_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteEventBreakerResponse](../../models/operations/deleteeventbreakerresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## post

Create Event Breaker Ruleset

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.EventBreakerRuleset(
    id='<ID>',
    rules=[
        components.EventBreakerRulesetRules(
            definitions=components.Definitions(
                fields=[
                    'string',
                ],
                keep=[
                    'string',
                ],
                remove=[
                    'string',
                ],
            ),
            fields=[
                components.Fields(
                    value='string',
                ),
            ],
            name='string',
            timestamp=components.EventBreakerRulesetTimestampFormat(),
        ),
    ],
)

res = s.event_breaker.post(req)

if res.event_breaker_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.EventBreakerRuleset](../../models/components/eventbreakerruleset.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PostEventBreakerResponse](../../models/operations/posteventbreakerresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update Event Breaker Ruleset

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.event_breaker.update(id='string', event_breaker_ruleset=components.EventBreakerRuleset(
    id='<ID>',
    rules=[
        components.EventBreakerRulesetRules(
            definitions=components.Definitions(
                fields=[
                    'string',
                ],
                keep=[
                    'string',
                ],
                remove=[
                    'string',
                ],
            ),
            fields=[
                components.Fields(
                    value='string',
                ),
            ],
            name='string',
            timestamp=components.EventBreakerRulesetTimestampFormat(),
        ),
    ],
))

if res.event_breaker_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | Unique ID                                                                                  |
| `event_breaker_ruleset`                                                                    | [Optional[components.EventBreakerRuleset]](../../models/components/eventbreakerruleset.md) | :heavy_minus_sign:                                                                         | Event Breaker Ruleset object to be updated                                                 |


### Response

**[operations.UpdateEventBreakerResponse](../../models/operations/updateeventbreakerresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
