# EventBreaker

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


res = s.event_breaker.delete(id='quod')

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
    description='nam',
    id='e61e6b7b-95bc-40ab-bc20-c4f3789fd871',
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=951875,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='error',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='sint',
                field_filter_expr='pariatur',
                fields_=[
                    'possimus',
                ],
                keep=[
                    'quia',
                ],
                remove=[
                    'eveniet',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Carroll Bogan V',
                    value='culpa',
                ),
            ],
            max_event_bytes=398434,
            name='Scott Wehner',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='eius',
                length=727697,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
            ),
            timestamp_anchor_regex='soluta',
            timestamp_earliest='accusantium',
            timestamp_latest='aliquam',
            timestamp_timezone='sapiente',
            type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
        ),
    ],
    tags='ullam',
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


res = s.event_breaker.update(id='reprehenderit', event_breaker_ruleset=shared.EventBreakerRuleset(
    description='ullam',
    id='6082d68e-a19f-41d1-b051-339d08086a18',
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=251941,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='voluptatem',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='dolor',
                field_filter_expr='occaecati',
                fields_=[
                    'numquam',
                ],
                keep=[
                    'impedit',
                ],
                remove=[
                    'explicabo',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Dr. Maria Kulas',
                    value='velit',
                ),
            ],
            max_event_bytes=974257,
            name='Tabitha Bayer',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='consequuntur',
                length=831520,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
            ),
            timestamp_anchor_regex='maxime',
            timestamp_earliest='dignissimos',
            timestamp_latest='officia',
            timestamp_timezone='asperiores',
            type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
        ),
    ],
    tags='quae',
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

