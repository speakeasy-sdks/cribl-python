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
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.event_breaker.delete(id='program')

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


## post

Create Event Breaker Ruleset

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.EventBreakerRuleset(
    id='<ID>',
    rules=[
        shared.EventBreakerRulesetRules(
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                fields_=[
                    'payment',
                ],
                keep=[
                    'Silver',
                ],
                remove=[
                    'iste',
                ],
            ),
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    value='protocol off beside',
                ),
            ],
            name='Arizona synthesizing',
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(),
        ),
    ],
)

res = s.event_breaker.post(req)

if res.event_breaker_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.EventBreakerRuleset](../../models/shared/eventbreakerruleset.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.PostEventBreakerResponse](../../models/operations/posteventbreakerresponse.md)**


## update

Update Event Breaker Ruleset

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.event_breaker.update(id='Van', event_breaker_ruleset=shared.EventBreakerRuleset(
    id='<ID>',
    rules=[
        shared.EventBreakerRulesetRules(
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                fields_=[
                    'East',
                ],
                keep=[
                    'male',
                ],
                remove=[
                    'Metal',
                ],
            ),
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    value='Arizona Cotton extend',
                ),
            ],
            name='bifurcated',
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(),
        ),
    ],
))

if res.event_breaker_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | Unique ID                                                                          |
| `event_breaker_ruleset`                                                            | [Optional[shared.EventBreakerRuleset]](../../models/shared/eventbreakerruleset.md) | :heavy_minus_sign:                                                                 | Event Breaker Ruleset object to be updated                                         |


### Response

**[operations.UpdateEventBreakerResponse](../../models/operations/updateeventbreakerresponse.md)**

