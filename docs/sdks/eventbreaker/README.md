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

req = operations.DeleteEventBreakerRequest(
    id='ac600dec-001a-4c80-ae2e-c09ff8f0f816',
)

res = s.event_breaker.delete(req)

if res.event_breaker_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteEventBreakerRequest](../../models/operations/deleteeventbreakerrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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
    description='earum',
    id='f3477c13-e902-4c14-925b-0960a668151a',
    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
    min_raw_length=278116,
    rules=[
        shared.EventBreakerRulesetRules(
            condition='magni',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='deserunt',
                field_filter_expr='delectus',
                fields_=[
                    'sed',
                    'nesciunt',
                    'maxime',
                ],
                keep=[
                    'cupiditate',
                    'aliquam',
                ],
                remove=[
                    'maiores',
                    'laudantium',
                    'velit',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Renee Beer',
                    value='quas',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Elsie Yundt',
                    value='perspiciatis',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Mildred Schinner',
                    value='porro',
                ),
                shared.EventBreakerRulesetRulesFields(
                    name='Abraham Gleason',
                    value='eius',
                ),
            ],
            max_event_bytes=194058,
            name='Marlon Koelpin',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='repellat',
                length=955047,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
            ),
            timestamp_anchor_regex='maiores',
            timestamp_earliest='itaque',
            timestamp_latest='nulla',
            timestamp_timezone='deserunt',
            type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
        ),
        shared.EventBreakerRulesetRules(
            condition='velit',
            definitions=shared.EventBreakerRulesetRulesDefinitions(
                dst_field='officiis',
                field_filter_expr='enim',
                fields_=[
                    'saepe',
                    'eum',
                    'repudiandae',
                ],
                keep=[
                    'officia',
                ],
                remove=[
                    'quasi',
                    'blanditiis',
                    'eius',
                    'quisquam',
                ],
            ),
            disabled=False,
            fields_=[
                shared.EventBreakerRulesetRulesFields(
                    name='Jeremiah Schimmel',
                    value='reprehenderit',
                ),
            ],
            max_event_bytes=800799,
            name='Byron Farrell',
            parser_enabled=False,
            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                format='laborum',
                length=266946,
                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
            ),
            timestamp_anchor_regex='necessitatibus',
            timestamp_earliest='architecto',
            timestamp_latest='molestias',
            timestamp_timezone='dolore',
            type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
        ),
    ],
    tags='maiores',
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

req = operations.UpdateEventBreakerRequest(
    event_breaker_ruleset=shared.EventBreakerRuleset(
        description='neque',
        id='2e550557-56f5-4d56-90bd-0af2dfe13db4',
        lib=shared.EventBreakerRulesetLibrary.CUSTOM,
        min_raw_length=976762,
        rules=[
            shared.EventBreakerRulesetRules(
                condition='explicabo',
                definitions=shared.EventBreakerRulesetRulesDefinitions(
                    dst_field='minus',
                    field_filter_expr='soluta',
                    fields_=[
                        'velit',
                        'earum',
                        'praesentium',
                    ],
                    keep=[
                        'non',
                        'quasi',
                        'mollitia',
                    ],
                    remove=[
                        'harum',
                        'cumque',
                        'doloremque',
                        'expedita',
                    ],
                ),
                disabled=False,
                fields_=[
                    shared.EventBreakerRulesetRulesFields(
                        name='Sandy Hyatt',
                        value='tempora',
                    ),
                    shared.EventBreakerRulesetRulesFields(
                        name='Rodney Prohaska',
                        value='optio',
                    ),
                    shared.EventBreakerRulesetRulesFields(
                        name='Kim Ryan',
                        value='voluptatum',
                    ),
                ],
                max_event_bytes=614770,
                name='Dr. Ruth Blanda',
                parser_enabled=False,
                timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                    format='at',
                    length=823472,
                    type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                ),
                timestamp_anchor_regex='pariatur',
                timestamp_earliest='vel',
                timestamp_latest='sapiente',
                timestamp_timezone='mollitia',
                type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
            ),
            shared.EventBreakerRulesetRules(
                condition='quos',
                definitions=shared.EventBreakerRulesetRulesDefinitions(
                    dst_field='aperiam',
                    field_filter_expr='non',
                    fields_=[
                        'ad',
                        'aliquam',
                        'quisquam',
                        'quas',
                    ],
                    keep=[
                        'maiores',
                    ],
                    remove=[
                        'aliquid',
                    ],
                ),
                disabled=False,
                fields_=[
                    shared.EventBreakerRulesetRulesFields(
                        name='Rodney Jacobs',
                        value='rem',
                    ),
                    shared.EventBreakerRulesetRulesFields(
                        name='Allan Ferry',
                        value='blanditiis',
                    ),
                    shared.EventBreakerRulesetRulesFields(
                        name='Miss Emily Lemke DVM',
                        value='autem',
                    ),
                ],
                max_event_bytes=694088,
                name='Lowell Oberbrunner',
                parser_enabled=False,
                timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                    format='voluptas',
                    length=658199,
                    type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                ),
                timestamp_anchor_regex='alias',
                timestamp_earliest='fuga',
                timestamp_latest='aut',
                timestamp_timezone='dolore',
                type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
            ),
        ],
        tags='aliquam',
    ),
    id='95cc6991-71b5-41c1-bdb1-cf4b888ebdfc',
)

res = s.event_breaker.update(req)

if res.event_breaker_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateEventBreakerRequest](../../models/operations/updateeventbreakerrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateEventBreakerResponse](../../models/operations/updateeventbreakerresponse.md)**

