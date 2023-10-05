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
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=390366,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='Transexual protocol',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='Metrics synergize Arizona',
                field_filter_expr='Montana Hybrid',
                fields_=[
                    'content',
                ],
                keep=[
                    'intelligence',
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
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=991464,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='Quality',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='invoice Arizona',
                field_filter_expr='mostly',
                fields_=[
                    'withdrawal',
                ],
                keep=[
                    'extend',
                ],
                remove=[
                    'Plastic',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Forward',
                    value='immediately implement JBOD',
                ),
            ],
            max_event_bytes=771203,
            name='Representative Home',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='pascal Gasoline',
                length=439152,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
            ),
            timestamp_anchor_regex='Wooden Internal',
            timestamp_earliest='Dodge brightly',
            timestamp_latest='frictionless haptic modulo',
            timestamp_timezone='navigating Diesel Avon',
            type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
        ),
    ],
    tags='Reactive Global Northeast',
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

