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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.event_breaker.delete(id='program')

if res.event_breaker_rulesets is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.EventBreakerRuleset(
    description='Monitored needs-based parallelism',
    id='<ID>',
    lib='iste mealy',
    min_raw_length=42444,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='Metrics synergize Arizona',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='Montana Hybrid',
                field_filter_expr='withdrawal',
                fields_=[
                    'East',
                ],
                keep=[
                    'Southeast',
                ],
                remove=[
                    'array',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Clothing array Kids',
                    value='Integration HTTP',
                ),
            ],
            max_event_bytes=817236,
            name='down female compress',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='Dollar',
                length=845824,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
            ),
            timestamp_anchor_regex='deposit Bicycle France',
            timestamp_earliest='Customer Frozen',
            timestamp_latest='joule gullible',
            timestamp_timezone='Soul Mouse Clemente',
            type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
        ),
    ],
    tags='female Trigender Paradigm',
)

res = s.event_breaker.post(req)

if res.event_breaker_rulesets is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.event_breaker.update(id='Van', event_breaker_ruleset=shared.EventBreakerRuleset(
    description='Advanced encompassing orchestration',
    id='<ID>',
    lib='Metal cheater Islands',
    min_raw_length=499557,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='dynamic white',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='Carolina syndicate',
                field_filter_expr='implement JBOD',
                fields_=[
                    'Bicycle',
                ],
                keep=[
                    'guestbook',
                ],
                remove=[
                    'driver',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='pascal Gasoline',
                    value='Northeast Wooden',
                ),
            ],
            max_event_bytes=352919,
            name='Internal invoice',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='brightly',
                length=711564,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
            ),
            timestamp_anchor_regex='frictionless haptic',
            timestamp_earliest='possimus navigating Diesel',
            timestamp_latest='Greens',
            timestamp_timezone='hack Rubber',
            type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
        ),
    ],
    tags='West',
))

if res.event_breaker_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | Unique ID                                                                          |
| `event_breaker_ruleset`                                                            | [Optional[shared.EventBreakerRuleset]](../../models/shared/eventbreakerruleset.md) | :heavy_minus_sign:                                                                 | Event Breaker Ruleset object to be updated                                         |


### Response

**[operations.UpdateEventBreakerResponse](../../models/operations/updateeventbreakerresponse.md)**

