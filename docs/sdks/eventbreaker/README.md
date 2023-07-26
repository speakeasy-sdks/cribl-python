# event_breaker

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


res = s.event_breaker.delete('voluptatibus')

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
    description='quia',
    id='c4310661-e963-449e-9cf9-e06e3a437000',
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=639705,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='ea',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='quidem',
                field_filter_expr='voluptas',
                fields_=[
                    'placeat',
                    'perspiciatis',
                    'expedita',
                ],
                keep=[
                    'a',
                    'voluptate',
                    'ullam',
                ],
                remove=[
                    'necessitatibus',
                    'animi',
                    'impedit',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Jodi Mueller',
                    value='veritatis',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Mrs. Glenn Bruen',
                    value='qui',
                ),
            ],
            max_event_bytes=611328,
            name='Vivian Rodriguez',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='dolorum',
                length=487676,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
            ),
            timestamp_anchor_regex='alias',
            timestamp_earliest='magni',
            timestamp_latest='vel',
            timestamp_timezone='quae',
            type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
        ),
        shared.EventBreakerRulesetRules(
            condition='modi',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='neque',
                field_filter_expr='exercitationem',
                fields_=[
                    'et',
                    'ipsum',
                    'unde',
                    'nulla',
                ],
                keep=[
                    'maxime',
                    'quia',
                    'quia',
                ],
                remove=[
                    'omnis',
                    'libero',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Wm Steuber',
                    value='placeat',
                ),
            ],
            max_event_bytes=25756,
            name='Mr. Angela Volkman',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='dolore',
                length=755106,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
            ),
            timestamp_anchor_regex='voluptatem',
            timestamp_earliest='autem',
            timestamp_latest='esse',
            timestamp_timezone='dolores',
            type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
        ),
        shared.EventBreakerRulesetRules(
            condition='beatae',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='est',
                field_filter_expr='facere',
                fields_=[
                    'molestiae',
                    'provident',
                    'accusamus',
                ],
                keep=[
                    'tempore',
                    'sint',
                    'ea',
                    'autem',
                ],
                remove=[
                    'rerum',
                    'laudantium',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Boyd Rippin Sr.',
                    value='quidem',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Phil Barton',
                    value='eos',
                ),
            ],
            max_event_bytes=844854,
            name='Mrs. Mabel Connelly',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='earum',
                length=239337,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
            ),
            timestamp_anchor_regex='similique',
            timestamp_earliest='ut',
            timestamp_latest='quidem',
            timestamp_timezone='quis',
            type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
        ),
        shared.EventBreakerRulesetRules(
            condition='unde',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='molestiae',
                field_filter_expr='delectus',
                fields_=[
                    'fugit',
                    'numquam',
                    'numquam',
                ],
                keep=[
                    'at',
                ],
                remove=[
                    'dignissimos',
                    'optio',
                    'necessitatibus',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Kristy Lemke',
                    value='placeat',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Gladys King',
                    value='modi',
                ),
            ],
            max_event_bytes=357347,
            name='Tasha Wolff DDS',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='ratione',
                length=289913,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
            ),
            timestamp_anchor_regex='occaecati',
            timestamp_earliest='voluptas',
            timestamp_latest='quo',
            timestamp_timezone='velit',
            type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
        ),
    ],
    tags='fuga',
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


res = s.event_breaker.update('nostrum', shared.EventBreakerRuleset(
    description='est',
    id='cfbe2fd5-7075-4779-a917-7deac646ecb5',
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=463344,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='modi',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='ipsa',
                field_filter_expr='sint',
                fields_=[
                    'sequi',
                    'repudiandae',
                    'cum',
                    'dicta',
                ],
                keep=[
                    'veniam',
                    'animi',
                    'dolores',
                    'nam',
                ],
                remove=[
                    'consequuntur',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Larry Kuphal Sr.',
                    value='laboriosam',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Pete Mann',
                    value='aliquam',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Nettie Rosenbaum',
                    value='hic',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Willard Larson',
                    value='eaque',
                ),
            ],
            max_event_bytes=901163,
            name='Billie Morar',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='libero',
                length=244032,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
            ),
            timestamp_anchor_regex='delectus',
            timestamp_earliest='impedit',
            timestamp_latest='cum',
            timestamp_timezone='ipsum',
            type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
        ),
    ],
    tags='saepe',
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

