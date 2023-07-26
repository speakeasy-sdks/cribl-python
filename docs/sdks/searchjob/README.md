# search_job

### Available Operations

* [create](#create) - Create SearchJob
* [delete](#delete) - Delete SearchJob
* [get](#get) - Get SearchJob by ID
* [update](#update) - Update SearchJob

## create

Create SearchJob

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            x_axis='officia',
            y_axis=[
                'animi',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='quas',
                data=[
                    {
                        "quo": 'ullam',
                        "ipsa": 'placeat',
                        "quas": 'culpa',
                        "consectetur": 'nostrum',
                    },
                    {
                        "eos": 'porro',
                    },
                    {
                        "dolorem": 'voluptate',
                        "blanditiis": 'dolore',
                    },
                    {
                        "provident": 'dolorem',
                        "alias": 'dignissimos',
                        "minima": 'eaque',
                    },
                ],
                data_expression='mollitia',
                data_filter={
                    "sit": 'accusamus',
                },
                name='Leslie Hodkiewicz',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='ducimus',
                data=[
                    {
                        "possimus": 'dolore',
                        "neque": 'inventore',
                    },
                ],
                data_expression='omnis',
                data_filter={
                    "nesciunt": 'omnis',
                    "corrupti": 'optio',
                },
                name='Penny Fadel',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='quia',
                data=[
                    {
                        "praesentium": 'accusamus',
                        "fugiat": 'ipsum',
                        "pariatur": 'amet',
                    },
                ],
                data_expression='deserunt',
                data_filter={
                    "quam": 'placeat',
                    "est": 'non',
                    "placeat": 'veniam',
                },
                name='Otis Lowe',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='error',
                data=[
                    {
                        "perferendis": 'impedit',
                        "reiciendis": 'quibusdam',
                    },
                    {
                        "pariatur": 'commodi',
                        "iste": 'corrupti',
                    },
                    {
                        "distinctio": 'in',
                        "consequuntur": 'voluptatem',
                        "voluptas": 'magnam',
                    },
                ],
                data_expression='ad',
                data_filter={
                    "ipsa": 'iure',
                },
                name='Desiree Bogisich',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='laborum',
            color_palette=529677,
            type='ratione',
        ),
        single_value=shared.SingleValue(
            color='facere',
            decimals=261953,
            label='perspiciatis',
            prefix='consequuntur',
            suffix='earum',
            type='quibusdam',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    280313,
                ],
            ),
            type='tempore',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='molestias',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=682724,
        total_exec_cpu_seconds=141128,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='sunt',
                id='954545e9-55dc-4c18-9ea4-901c7c43ad2d',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=670566,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='quam',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='totam',
                            field_filter_expr='incidunt',
                            fields_=[
                                'nobis',
                                'culpa',
                                'ratione',
                            ],
                            keep=[
                                'sed',
                                'amet',
                                'aut',
                                'voluptates',
                            ],
                            remove=[
                                'tenetur',
                                'dignissimos',
                                'dolor',
                                'totam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Mrs. Maggie Breitenberg',
                                value='laudantium',
                            ),
                        ],
                        max_event_bytes=164154,
                        name='Orville Kutch',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='enim',
                            length=377392,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='voluptatem',
                        timestamp_earliest='quam',
                        timestamp_latest='vel',
                        timestamp_timezone='aspernatur',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='porro',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='ad',
                            field_filter_expr='deleniti',
                            fields_=[
                                'magnam',
                                'nulla',
                                'iusto',
                                'adipisci',
                            ],
                            keep=[
                                'voluptas',
                                'nostrum',
                                'eum',
                            ],
                            remove=[
                                'cumque',
                                'fugit',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Mr. Brian Kihn',
                                value='omnis',
                            ),
                        ],
                        max_event_bytes=414547,
                        name='Desiree Collier',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='dignissimos',
                            length=860411,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='libero',
                        timestamp_earliest='corrupti',
                        timestamp_latest='doloribus',
                        timestamp_timezone='enim',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='sed',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='assumenda',
                            field_filter_expr='atque',
                            fields_=[
                                'odit',
                                'eligendi',
                                'earum',
                            ],
                            keep=[
                                'atque',
                                'sunt',
                            ],
                            remove=[
                                'placeat',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Julie Crooks',
                                value='esse',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Miss Bruce Gibson',
                                value='corporis',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Nora Wilderman',
                                value='hic',
                            ),
                        ],
                        max_event_bytes=503015,
                        name='Henry Pollich DDS',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='quod',
                            length=518728,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='dicta',
                        timestamp_earliest='maiores',
                        timestamp_latest='dolores',
                        timestamp_timezone='perferendis',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='nulla',
            ),
            shared.EventBreakerRuleset(
                description='corporis',
                id='d831d008-1090-4f67-8667-3f3a681c5768',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=830003,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='itaque',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='molestiae',
                            field_filter_expr='quaerat',
                            fields_=[
                                'dolore',
                            ],
                            keep=[
                                'excepturi',
                            ],
                            remove=[
                                'odit',
                                'beatae',
                                'exercitationem',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Mr. Mattie Hoeger',
                                value='molestias',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Homer Harber',
                                value='sequi',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Luis O'Connell',
                                value='pariatur',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Luther Spencer',
                                value='dolorem',
                            ),
                        ],
                        max_event_bytes=243965,
                        name='Clark Stroman',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='incidunt',
                            length=508373,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='itaque',
                        timestamp_earliest='non',
                        timestamp_latest='dolorum',
                        timestamp_timezone='esse',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='natus',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='quas',
                            field_filter_expr='saepe',
                            fields_=[
                                'assumenda',
                                'maiores',
                            ],
                            keep=[
                                'in',
                            ],
                            remove=[
                                'quaerat',
                                'nostrum',
                                'libero',
                                'totam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Bernice Schultz I',
                                value='recusandae',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Tiffany Muller',
                                value='dolores',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Jean Bednar III',
                                value='cum',
                            ),
                        ],
                        max_event_bytes=816900,
                        name='Erica Gleichner V',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='sed',
                            length=687643,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='nihil',
                        timestamp_earliest='velit',
                        timestamp_latest='incidunt',
                        timestamp_timezone='a',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='consequuntur',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='numquam',
                            field_filter_expr='numquam',
                            fields_=[
                                'pariatur',
                                'voluptatum',
                                'vel',
                            ],
                            keep=[
                                'modi',
                                'expedita',
                                'quidem',
                                'consequuntur',
                            ],
                            remove=[
                                'asperiores',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Mr. Mona McLaughlin',
                                value='expedita',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Dexter Kulas',
                                value='placeat',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Courtney Gleichner',
                                value='sed',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Marta Jakubowski',
                                value='consequuntur',
                            ),
                        ],
                        max_event_bytes=797903,
                        name='Merle Keebler Jr.',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='debitis',
                            length=606529,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='quidem',
                        timestamp_earliest='neque',
                        timestamp_latest='est',
                        timestamp_timezone='repellendus',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='quisquam',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='vel',
                            field_filter_expr='cum',
                            fields_=[
                                'adipisci',
                            ],
                            keep=[
                                'accusantium',
                            ],
                            remove=[
                                'facere',
                                'occaecati',
                                'quisquam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Arlene Gislason',
                                value='aut',
                            ),
                        ],
                        max_event_bytes=523613,
                        name='Jeannette Muller',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='eos',
                            length=650392,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='dicta',
                        timestamp_earliest='earum',
                        timestamp_latest='possimus',
                        timestamp_timezone='nemo',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='iusto',
            ),
            shared.EventBreakerRuleset(
                description='veritatis',
                id='e9c32635-0a46-4714-b789-ce0e991594d9',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=228483,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='ducimus',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='modi',
                            field_filter_expr='impedit',
                            fields_=[
                                'dolores',
                            ],
                            keep=[
                                'sed',
                                'a',
                            ],
                            remove=[
                                'dolor',
                                'quidem',
                                'quaerat',
                                'cum',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Ira Lindgren',
                                value='reprehenderit',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Pat Raynor',
                                value='officiis',
                            ),
                        ],
                        max_event_bytes=95168,
                        name='Brandon Rutherford',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='eaque',
                            length=136851,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='laborum',
                        timestamp_earliest='hic',
                        timestamp_latest='rerum',
                        timestamp_timezone='explicabo',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='nam',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='placeat',
                            field_filter_expr='aliquam',
                            fields_=[
                                'adipisci',
                                'ipsam',
                            ],
                            keep=[
                                'enim',
                                'eveniet',
                                'eum',
                                'exercitationem',
                            ],
                            remove=[
                                'culpa',
                                'alias',
                                'eos',
                                'quos',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Sophia Marvin MD',
                                value='veritatis',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Philip Armstrong',
                                value='deserunt',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Franklin Jerde',
                                value='occaecati',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Adrian Reichert',
                                value='laboriosam',
                            ),
                        ],
                        max_event_bytes=487652,
                        name='Kelley Boehm',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='quasi',
                            length=177250,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='vel',
                        timestamp_earliest='rerum',
                        timestamp_latest='cupiditate',
                        timestamp_timezone='excepturi',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.REGEX,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='eius',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='perspiciatis',
                            field_filter_expr='dolore',
                            fields_=[
                                'natus',
                                'numquam',
                            ],
                            keep=[
                                'corrupti',
                                'ducimus',
                            ],
                            remove=[
                                'veniam',
                                'cumque',
                                'praesentium',
                                'ut',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Antonio Jaskolski',
                                value='laboriosam',
                            ),
                        ],
                        max_event_bytes=691549,
                        name='Adrienne Stokes',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='dolore',
                            length=115870,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='facilis',
                        timestamp_earliest='sit',
                        timestamp_latest='incidunt',
                        timestamp_timezone='magnam',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                ],
                tags='hic',
            ),
            shared.EventBreakerRuleset(
                description='error',
                id='df13f4ee-dbe7-48bf-a068-25894ea763d5',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=771363,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='fugit',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='voluptate',
                            field_filter_expr='provident',
                            fields_=[
                                'expedita',
                                'quam',
                            ],
                            keep=[
                                'exercitationem',
                                'vitae',
                                'magnam',
                            ],
                            remove=[
                                'nulla',
                                'eum',
                                'quibusdam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Misty Toy',
                                value='consectetur',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Whitney Emard',
                                value='maxime',
                            ),
                        ],
                        max_event_bytes=29144,
                        name='Dr. Austin Kiehn',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='magni',
                            length=973003,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='provident',
                        timestamp_earliest='delectus',
                        timestamp_latest='dolore',
                        timestamp_timezone='totam',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='numquam',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='sunt',
                            field_filter_expr='consequuntur',
                            fields_=[
                                'voluptates',
                                'in',
                            ],
                            keep=[
                                'expedita',
                                'ducimus',
                            ],
                            remove=[
                                'eum',
                                'doloremque',
                                'iure',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Gary Weber',
                                value='vel',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Wade Dicki',
                                value='alias',
                            ),
                        ],
                        max_event_bytes=685507,
                        name='Lola Leuschke',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='veniam',
                            length=724307,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='vitae',
                        timestamp_earliest='explicabo',
                        timestamp_latest='corporis',
                        timestamp_timezone='incidunt',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                ],
                tags='nihil',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=239185,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'reiciendis',
            'dolore',
            'voluptatibus',
        ],
    ),
    group='eveniet',
    id='77210d1f-6558-4c99-8722-d2bc0f94087d',
    latest_epoch=599413,
    num_events_after=806901,
    num_events_before=634880,
    query='deserunt',
    sample_rate=926879,
    search_config=shared.SearchConfig(
        datasets=[
            'magnam',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'quibusdam',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='voluptate',
            ),
            shared.SearchTerm(
                is_case_sensitive=False,
                term='placeat',
            ),
            shared.SearchTerm(
                is_case_sensitive=False,
                term='est',
            ),
            shared.SearchTerm(
                is_case_sensitive=False,
                term='est',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='nam',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='id',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='quod',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='sint',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='minima',
            name='Mrs. Dominick Mann',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    search_parameter_values='ducimus',
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='amet',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='ducimus',
            precision='deleniti',
            prefix='dolor',
            suffix='ab',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='sint',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='quos',
        ),
        row_number_column_width=193200,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=262824,
    time_completed=140972,
    time_created=924872,
    time_started=325352,
    type=shared.SearchJobType.STANDARD,
    user='similique',
)

res = s.search_job.create(req)

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.SearchJob](../../models/shared/searchjob.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.CreateSearchJobResponse](../../models/operations/createsearchjobresponse.md)**


## delete

Delete SearchJob

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteSearchJobRequest(
    id='85466597-c502-433c-9471-d51aaa6ddf5a',
)

res = s.search_job.delete(req)

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteSearchJobRequest](../../models/operations/deletesearchjobrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.DeleteSearchJobResponse](../../models/operations/deletesearchjobresponse.md)**


## get

Get SearchJob by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSearchJobRequest(
    id='bd6487c5-fc2b-4862-a00b-ef69e1001576',
)

res = s.search_job.get(req)

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetSearchJobRequest](../../models/operations/getsearchjobrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetSearchJobResponse](../../models/operations/getsearchjobresponse.md)**


## update

Update SearchJob

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateSearchJobRequest(
    search_job=shared.SearchJob(
        chart_config=shared.ChartConfig(
            axis=shared.ChartConfigAxis(
                x_axis='dolor',
                y_axis=[
                    'libero',
                ],
            ),
            legend=shared.Legend(),
            series=[
                shared.ChartSeries(
                    color='fuga',
                    data=[
                        {
                            "repellat": 'quibusdam',
                            "accusamus": 'illum',
                            "blanditiis": 'tempora',
                        },
                        {
                            "dolor": 'enim',
                            "dolorum": 'aliquam',
                            "beatae": 'explicabo',
                        },
                    ],
                    data_expression='nesciunt',
                    data_filter={
                        "officiis": 'inventore',
                        "officia": 'in',
                        "sequi": 'ad',
                    },
                    name='Sylvester Dibbert',
                    type=shared.ChartType(),
                ),
                shared.ChartSeries(
                    color='saepe',
                    data=[
                        {
                            "expedita": 'itaque',
                        },
                    ],
                    data_expression='maiores',
                    data_filter={
                        "dignissimos": 'dicta',
                        "id": 'blanditiis',
                        "repellat": 'modi',
                    },
                    name='Gayle Schroeder Jr.',
                    type=shared.ChartType(),
                ),
                shared.ChartSeries(
                    color='aut',
                    data=[
                        {
                            "officiis": 'omnis',
                            "ea": 'ipsam',
                            "soluta": 'esse',
                            "vitae": 'beatae',
                        },
                        {
                            "voluptatem": 'blanditiis',
                            "eligendi": 'tenetur',
                            "deleniti": 'deleniti',
                            "necessitatibus": 'cumque',
                        },
                    ],
                    data_expression='iste',
                    data_filter={
                        "nihil": 'libero',
                        "perspiciatis": 'occaecati',
                        "officia": 'nemo',
                        "quis": 'doloremque',
                    },
                    name='Andre Hayes',
                    type=shared.ChartType(),
                ),
                shared.ChartSeries(
                    color='possimus',
                    data=[
                        {
                            "velit": 'soluta',
                        },
                    ],
                    data_expression='cum',
                    data_filter={
                        "quo": 'officiis',
                    },
                    name='Carlton Paucek',
                    type=shared.ChartType(),
                ),
            ],
            settings=shared.Settings(
                color='modi',
                color_palette=231283,
                type='qui',
            ),
            single_value=shared.SingleValue(
                color='officia',
                decimals=585645,
                label='rem',
                prefix='ea',
                suffix='debitis',
                type='soluta',
            ),
            x_axis=shared.Axis(
                axis_label=shared.AxisLabel(
                    formatter=shared.AxisLabelFormatter(),
                    formatter_data=[
                        906775,
                        108879,
                    ],
                ),
                type='dolore',
            ),
        ),
        compatibility_checks=shared.SearchJobCompatibilityChecks(
            datatypes=False,
        ),
        correlation_id='quisquam',
        cpu_metrics=shared.CPUTimeMetric(
            total_cpu_seconds=649901,
            total_exec_cpu_seconds=370219,
        ),
        datatype_overrides=shared.DatatypeOverrides(
            breaker_rulesets=[
                shared.EventBreakerRuleset(
                    description='non',
                    id='08915009-7019-4a48-b88e-ce7bf904e011',
                    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                    min_raw_length=25476,
                    rules=[
                        shared.EventBreakerRulesetRules(
                            condition='temporibus',
                            definitions=shared.EventBreakerRulesetRulesDefinitions(
                                dst_field='sequi',
                                field_filter_expr='laudantium',
                                fields_=[
                                    'alias',
                                    'deleniti',
                                    'quasi',
                                ],
                                keep=[
                                    'aspernatur',
                                    'quod',
                                ],
                                remove=[
                                    'tempore',
                                    'recusandae',
                                ],
                            ),
                            disabled=False,
                            fields_=[
                                shared.EventBreakerRulesetRulesFields(
                                    name='Dr. Mattie Nader',
                                    value='enim',
                                ),
                                shared.EventBreakerRulesetRulesFields(
                                    name='Alison King I',
                                    value='mollitia',
                                ),
                                shared.EventBreakerRulesetRulesFields(
                                    name='Dr. Carrie Lang',
                                    value='at',
                                ),
                            ],
                            max_event_bytes=920548,
                            name='Ms. Helen West',
                            parser_enabled=False,
                            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                                format='fugiat',
                                length=542986,
                                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                            ),
                            timestamp_anchor_regex='aut',
                            timestamp_earliest='commodi',
                            timestamp_latest='architecto',
                            timestamp_timezone='atque',
                            type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                        ),
                        shared.EventBreakerRulesetRules(
                            condition='unde',
                            definitions=shared.EventBreakerRulesetRulesDefinitions(
                                dst_field='voluptate',
                                field_filter_expr='debitis',
                                fields_=[
                                    'ad',
                                ],
                                keep=[
                                    'aspernatur',
                                ],
                                remove=[
                                    'molestiae',
                                    'minima',
                                    'et',
                                ],
                            ),
                            disabled=False,
                            fields_=[
                                shared.EventBreakerRulesetRulesFields(
                                    name='Mrs. Oliver Legros Sr.',
                                    value='quia',
                                ),
                            ],
                            max_event_bytes=591082,
                            name='Della Ruecker DDS',
                            parser_enabled=False,
                            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                                format='sed',
                                length=674287,
                                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                            ),
                            timestamp_anchor_regex='eaque',
                            timestamp_earliest='odit',
                            timestamp_latest='distinctio',
                            timestamp_timezone='soluta',
                            type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                        ),
                    ],
                    tags='odio',
                ),
                shared.EventBreakerRuleset(
                    description='repudiandae',
                    id='e102da2d-e35f-48e0-9bf3-3eaab45402ac',
                    lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                    min_raw_length=121860,
                    rules=[
                        shared.EventBreakerRulesetRules(
                            condition='voluptatem',
                            definitions=shared.EventBreakerRulesetRulesDefinitions(
                                dst_field='incidunt',
                                field_filter_expr='soluta',
                                fields_=[
                                    'vitae',
                                    'maxime',
                                    'placeat',
                                    'cupiditate',
                                ],
                                keep=[
                                    'maxime',
                                    'ex',
                                    'dicta',
                                    'deserunt',
                                ],
                                remove=[
                                    'itaque',
                                    'ad',
                                    'voluptates',
                                ],
                            ),
                            disabled=False,
                            fields_=[
                                shared.EventBreakerRulesetRulesFields(
                                    name='Dixie Balistreri',
                                    value='molestias',
                                ),
                                shared.EventBreakerRulesetRulesFields(
                                    name='Patty Hermiston',
                                    value='incidunt',
                                ),
                                shared.EventBreakerRulesetRulesFields(
                                    name='Ronald Leffler',
                                    value='odit',
                                ),
                            ],
                            max_event_bytes=385770,
                            name='Genevieve Orn',
                            parser_enabled=False,
                            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                                format='esse',
                                length=609364,
                                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                            ),
                            timestamp_anchor_regex='ipsum',
                            timestamp_earliest='minus',
                            timestamp_latest='molestiae',
                            timestamp_timezone='illo',
                            type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                        ),
                        shared.EventBreakerRulesetRules(
                            condition='placeat',
                            definitions=shared.EventBreakerRulesetRulesDefinitions(
                                dst_field='sequi',
                                field_filter_expr='et',
                                fields_=[
                                    'voluptates',
                                    'cumque',
                                    'distinctio',
                                ],
                                keep=[
                                    'consectetur',
                                    'nulla',
                                    'magni',
                                ],
                                remove=[
                                    'esse',
                                ],
                            ),
                            disabled=False,
                            fields_=[
                                shared.EventBreakerRulesetRulesFields(
                                    name='Rogelio Doyle',
                                    value='maxime',
                                ),
                                shared.EventBreakerRulesetRulesFields(
                                    name='Rosa Stokes',
                                    value='ad',
                                ),
                                shared.EventBreakerRulesetRulesFields(
                                    name='Madeline Mitchell',
                                    value='error',
                                ),
                            ],
                            max_event_bytes=304459,
                            name='Tommy Rippin',
                            parser_enabled=False,
                            timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                                format='nihil',
                                length=61877,
                                type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                            ),
                            timestamp_anchor_regex='tenetur',
                            timestamp_earliest='eaque',
                            timestamp_latest='ex',
                            timestamp_timezone='rerum',
                            type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                        ),
                    ],
                    tags='laudantium',
                ),
            ],
            disable_breakers=False,
        ),
        earliest_epoch=921981,
        error_state_config=shared.SearchJobErrorStateConfig(
            coordinated=False,
            error_messages=[
                'porro',
                'atque',
                'autem',
                'eius',
            ],
        ),
        group='unde',
        id='2386f62c-969c-44cc-ab78-890a3fd3c81d',
        latest_epoch=634898,
        num_events_after=119473,
        num_events_before=20735,
        query='asperiores',
        sample_rate=534204,
        search_config=shared.SearchConfig(
            datasets=[
                'consequuntur',
                'non',
                'fugiat',
                'voluptatibus',
            ],
            has_send_operator=False,
            ordered_field_names=[
                'amet',
                'quae',
                'pariatur',
            ],
            search_terms=[
                shared.SearchTerm(
                    is_case_sensitive=False,
                    term='velit',
                ),
                shared.SearchTerm(
                    is_case_sensitive=False,
                    term='debitis',
                ),
                shared.SearchTerm(
                    is_case_sensitive=False,
                    term='facere',
                ),
            ],
            sort_fields=[
                shared.SortByField(
                    direction=shared.SortByFieldDirection.ASCENDING,
                    field_name='vitae',
                    null_position=shared.SortByFieldNullPosition.NULLS_LAST,
                ),
                shared.SortByField(
                    direction=shared.SortByFieldDirection.DESCENDING,
                    field_name='facere',
                    null_position=shared.SortByFieldNullPosition.NULLS_LAST,
                ),
                shared.SortByField(
                    direction=shared.SortByFieldDirection.ASCENDING,
                    field_name='similique',
                    null_position=shared.SortByFieldNullPosition.NULLS_LAST,
                ),
            ],
            suppress_event_marking=False,
            use_formatted_visualization=False,
        ),
        search_parameter_declarations=[
            shared.SearchParameter(
                default_value='sint',
                name='Mrs. Edith Hermiston',
                type=shared.SearchParameterType.NUMBER,
            ),
            shared.SearchParameter(
                default_value='magni',
                name='Doreen Boehm',
                type=shared.SearchParameterType.STRING,
            ),
            shared.SearchParameter(
                default_value='dicta',
                name='Morris Flatley',
                type=shared.SearchParameterType.STRING,
            ),
            shared.SearchParameter(
                default_value='aliquid',
                name='Ms. Brent Marquardt DVM',
                type=shared.SearchParameterType.BOOLEAN,
            ),
        ],
        search_parameter_values='iure',
        status=shared.SearchJobStatus.NEW,
        table_config=shared.TableViewSettings(
            column_filter_settings=shared.ColumnFilterSettings(
                contains='accusamus',
            ),
            column_format_settings=shared.ColumnFormatSettings(
                palette='cum',
                precision='occaecati',
                prefix='fuga',
                suffix='ex',
            ),
            column_order_settings=shared.ColumnOrderSettings(
                order='autem',
            ),
            column_sort_settings=shared.ColumnSortSettings(
                sort='nostrum',
            ),
            row_number_column_width=540833,
            show_column_totals=False,
            show_column_totals_pinned=False,
            show_row_numbers=False,
            show_row_totals=False,
            show_row_totals_pinned=False,
            view_mode=shared.TableViewSettingsViewMode.TABLE,
        ),
        target_event_time=432055,
        time_completed=565245,
        time_created=684196,
        time_started=251713,
        type=shared.SearchJobType.SCHEDULED,
        user='totam',
    ),
    id='43d382db-ec75-4c68-8606-59468ce304d8',
)

res = s.search_job.update(req)

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateSearchJobRequest](../../models/operations/updatesearchjobrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateSearchJobResponse](../../models/operations/updatesearchjobresponse.md)**

