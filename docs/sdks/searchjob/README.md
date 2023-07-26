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
            x_axis='numquam',
            y_axis=[
                'eligendi',
                'sapiente',
                'alias',
                'impedit',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='aspernatur',
                data=[
                    {
                        "voluptatum": 'reiciendis',
                        "vitae": 'ullam',
                    },
                    {
                        "consequuntur": 'voluptas',
                        "ratione": 'excepturi',
                    },
                    {
                        "est": 'perferendis',
                        "quibusdam": 'impedit',
                        "ducimus": 'nisi',
                    },
                ],
                data_expression='nisi',
                data_filter={
                    "fugit": 'dolore',
                },
                name='Ms. Wilbert Ratke',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='totam',
                data=[
                    {
                        "inventore": 'consequuntur',
                        "repellendus": 'sit',
                        "dolores": 'enim',
                    },
                    {
                        "perspiciatis": 'magni',
                    },
                    {
                        "alias": 'quidem',
                        "deleniti": 'possimus',
                    },
                    {
                        "odio": 'fugit',
                        "aspernatur": 'at',
                    },
                ],
                data_expression='illum',
                data_filter={
                    "sint": 'exercitationem',
                    "cum": 'voluptatum',
                    "facilis": 'placeat',
                },
                name='Ernest Grimes',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='cupiditate',
            color_palette=365676,
            type='natus',
        ),
        single_value=shared.SingleValue(
            color='nisi',
            decimals=588542,
            label='amet',
            prefix='dolor',
            suffix='nostrum',
            type='qui',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    477352,
                    292571,
                    356343,
                    245990,
                ],
            ),
            type='adipisci',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='cupiditate',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=581269,
        total_exec_cpu_seconds=258036,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='molestiae',
                id='8de3b6e9-389f-45ab-b7f6-62550a28382a',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=754784,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='deleniti',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='dolor',
                            field_filter_expr='est',
                            fields_=[
                                'possimus',
                                'odit',
                                'consectetur',
                                'inventore',
                            ],
                            keep=[
                                'facilis',
                                'facilis',
                            ],
                            remove=[
                                'nisi',
                                'ipsam',
                                'voluptatem',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Ms. Eva Upton',
                                value='veniam',
                            ),
                        ],
                        max_event_bytes=695408,
                        name='Franklin Nolan',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='molestias',
                            length=102019,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='quisquam',
                        timestamp_earliest='praesentium',
                        timestamp_latest='facilis',
                        timestamp_timezone='assumenda',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='maiores',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='ipsum',
                            field_filter_expr='commodi',
                            fields_=[
                                'fugit',
                            ],
                            keep=[
                                'ex',
                                'neque',
                                'quod',
                            ],
                            remove=[
                                'alias',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Bryant Ondricka',
                                value='aperiam',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Constance Gislason',
                                value='deleniti',
                            ),
                        ],
                        max_event_bytes=638219,
                        name='Pablo Fahey',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='sit',
                            length=561399,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='expedita',
                        timestamp_earliest='voluptas',
                        timestamp_latest='maiores',
                        timestamp_timezone='ea',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='delectus',
            ),
            shared.EventBreakerRuleset(
                description='accusamus',
                id='f020e9f4-43b4-4257-b992-c8dbda6a61ef',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=661764,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='inventore',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='iste',
                            field_filter_expr='atque',
                            fields_=[
                                'ullam',
                            ],
                            keep=[
                                'doloribus',
                                'pariatur',
                                'aut',
                            ],
                            remove=[
                                'iste',
                                'eveniet',
                                'nam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Allison Wiza',
                                value='dolorem',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Randal Aufderhar',
                                value='aliquid',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Helen Stanton',
                                value='dicta',
                            ),
                        ],
                        max_event_bytes=538877,
                        name='Jean Schamberger',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='culpa',
                            length=837739,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='ad',
                        timestamp_earliest='cupiditate',
                        timestamp_latest='suscipit',
                        timestamp_timezone='reiciendis',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                ],
                tags='delectus',
            ),
            shared.EventBreakerRuleset(
                description='ab',
                id='ad837ae8-0c1c-419c-95ba-998678fa3f69',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=418787,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='cupiditate',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='ab',
                            field_filter_expr='fuga',
                            fields_=[
                                'dolor',
                                'voluptatum',
                                'molestias',
                                'quod',
                            ],
                            keep=[
                                'eaque',
                                'consectetur',
                                'autem',
                                'vitae',
                            ],
                            remove=[
                                'incidunt',
                                'modi',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Adrian Muller',
                                value='animi',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Silvia Wintheiser',
                                value='exercitationem',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Katie Bauch',
                                value='debitis',
                            ),
                        ],
                        max_event_bytes=951411,
                        name='Conrad Zulauf',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='aliquam',
                            length=71751,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='sed',
                        timestamp_earliest='necessitatibus',
                        timestamp_latest='possimus',
                        timestamp_timezone='dignissimos',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='explicabo',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='ullam',
                            field_filter_expr='non',
                            fields_=[
                                'incidunt',
                                'quod',
                                'sunt',
                                'ullam',
                            ],
                            keep=[
                                'illum',
                                'voluptates',
                            ],
                            remove=[
                                'est',
                                'in',
                                'illo',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Lucia Gorczany',
                                value='est',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Leland Wisoky',
                                value='quam',
                            ),
                        ],
                        max_event_bytes=686690,
                        name='Emanuel McKenzie',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='culpa',
                            length=855647,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='atque',
                        timestamp_earliest='ad',
                        timestamp_latest='sapiente',
                        timestamp_timezone='voluptates',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='nesciunt',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='ab',
                            field_filter_expr='quibusdam',
                            fields_=[
                                'quidem',
                                'delectus',
                            ],
                            keep=[
                                'cumque',
                                'voluptatum',
                            ],
                            remove=[
                                'atque',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Andres Larson',
                                value='eaque',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Archie Jaskolski',
                                value='minus',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Verna Gislason',
                                value='repudiandae',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Sergio Tremblay',
                                value='amet',
                            ),
                        ],
                        max_event_bytes=279679,
                        name='Tracy Witting',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='in',
                            length=609864,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='tenetur',
                        timestamp_earliest='recusandae',
                        timestamp_latest='expedita',
                        timestamp_timezone='iusto',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='harum',
            ),
            shared.EventBreakerRuleset(
                description='ad',
                id='c38d4baf-91e5-406e-b890-a54b475f16f5',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=405161,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='nesciunt',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='corrupti',
                            field_filter_expr='nostrum',
                            fields_=[
                                'sequi',
                                'maxime',
                                'numquam',
                            ],
                            keep=[
                                'eligendi',
                                'autem',
                                'adipisci',
                            ],
                            remove=[
                                'rerum',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Terence Considine',
                                value='eveniet',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Guy Will',
                                value='repellendus',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Mr. Virgil Greenfelder',
                                value='nisi',
                            ),
                        ],
                        max_event_bytes=245849,
                        name='Rudolph Weimann IV',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='atque',
                            length=243941,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='nam',
                        timestamp_earliest='aperiam',
                        timestamp_latest='vitae',
                        timestamp_timezone='mollitia',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='at',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='quibusdam',
                            field_filter_expr='quam',
                            fields_=[
                                'rem',
                                'vel',
                                'eos',
                            ],
                            keep=[
                                'sunt',
                                'blanditiis',
                            ],
                            remove=[
                                'accusamus',
                                'distinctio',
                                'incidunt',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Allan Feest',
                                value='accusantium',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Ms. Kim Zboncak',
                                value='tempore',
                            ),
                        ],
                        max_event_bytes=992244,
                        name='Marilyn Hilll',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='labore',
                            length=84438,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='magni',
                        timestamp_earliest='itaque',
                        timestamp_latest='error',
                        timestamp_timezone='expedita',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='placeat',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='temporibus',
                            field_filter_expr='voluptate',
                            fields_=[
                                'minima',
                                'odit',
                                'odit',
                                'eius',
                            ],
                            keep=[
                                'vel',
                                'dolorum',
                                'alias',
                            ],
                            remove=[
                                'ab',
                                'sunt',
                                'amet',
                                'cum',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Kyle Koch',
                                value='minima',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Rolando Brakus',
                                value='in',
                            ),
                        ],
                        max_event_bytes=995671,
                        name='Blanca Greenfelder',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='repudiandae',
                            length=273349,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='suscipit',
                        timestamp_earliest='illum',
                        timestamp_latest='iusto',
                        timestamp_timezone='aliquid',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='aliquid',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='repellat',
                            field_filter_expr='sapiente',
                            fields_=[
                                'eligendi',
                            ],
                            keep=[
                                'nihil',
                                'eius',
                            ],
                            remove=[
                                'corporis',
                                'perferendis',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Stacy Kovacek',
                                value='magnam',
                            ),
                        ],
                        max_event_bytes=981817,
                        name='Jean Welch',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='consequatur',
                            length=516739,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='quo',
                        timestamp_earliest='dolor',
                        timestamp_latest='sunt',
                        timestamp_timezone='omnis',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='officiis',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=118236,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'consectetur',
            'deserunt',
            'odit',
        ],
    ),
    group='incidunt',
    id='5467f948-74c2-4d5c-8497-2233e66bd8fe',
    latest_epoch=357867,
    num_events_after=830909,
    num_events_before=12917,
    query='voluptatem',
    sample_rate=727789,
    search_config=shared.SearchConfig(
        datasets=[
            'odio',
            'omnis',
            'officiis',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'magni',
            'sit',
            'velit',
            'voluptatum',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='neque',
            ),
            shared.SearchTerm(
                is_case_sensitive=False,
                term='aspernatur',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='cupiditate',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='quod',
            name='Joe Bartell',
            type=shared.SearchParameterType.STRING,
        ),
        shared.SearchParameter(
            default_value='aperiam',
            name='Sheila Brekke',
            type=shared.SearchParameterType.STRING,
        ),
        shared.SearchParameter(
            default_value='debitis',
            name='Cynthia Gottlieb',
            type=shared.SearchParameterType.NUMBER,
        ),
        shared.SearchParameter(
            default_value='ullam',
            name='Rogelio Kihn',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    search_parameter_values='ut',
    status=shared.SearchJobStatus.NEW,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='nihil',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='quam',
            precision='assumenda',
            prefix='consequatur',
            suffix='cumque',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='placeat',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='adipisci',
        ),
        row_number_column_width=950486,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    target_event_time=35107,
    time_completed=548473,
    time_created=933847,
    time_started=938015,
    type=shared.SearchJobType.SCHEDULED,
    user='dicta',
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


res = s.search_job.delete('corporis')

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.search_job.get('impedit')

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.search_job.update('eveniet', shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            x_axis='cum',
            y_axis=[
                'illum',
                'ea',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='quasi',
                data=[
                    {
                        "necessitatibus": 'voluptatem',
                        "maiores": 'odio',
                        "veniam": 'fuga',
                    },
                    {
                        "possimus": 'tenetur',
                        "sed": 'deserunt',
                        "eligendi": 'id',
                        "distinctio": 'corporis',
                    },
                    {
                        "soluta": 'cupiditate',
                        "unde": 'et',
                        "quisquam": 'unde',
                    },
                    {
                        "suscipit": 'facere',
                    },
                ],
                data_expression='pariatur',
                data_filter={
                    "quaerat": 'corrupti',
                    "sint": 'eius',
                    "vel": 'quasi',
                },
                name='Darren Funk DDS',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='nobis',
                data=[
                    {
                        "possimus": 'provident',
                        "veniam": 'sit',
                    },
                    {
                        "a": 'consequatur',
                    },
                    {
                        "id": 'error',
                        "ratione": 'perferendis',
                        "distinctio": 'voluptas',
                        "sint": 'maiores',
                    },
                    {
                        "fuga": 'cumque',
                        "consequuntur": 'maiores',
                    },
                ],
                data_expression='esse',
                data_filter={
                    "delectus": 'quos',
                },
                name='Miss Jon Bailey I',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='occaecati',
                data=[
                    {
                        "ex": 'doloremque',
                    },
                ],
                data_expression='quas',
                data_filter={
                    "perferendis": 'esse',
                },
                name='Nelson Langosh',
                type=shared.ChartType(),
            ),
            shared.ChartSeries(
                color='autem',
                data=[
                    {
                        "quos": 'consectetur',
                    },
                    {
                        "tenetur": 'necessitatibus',
                        "perspiciatis": 'suscipit',
                        "ullam": 'unde',
                    },
                ],
                data_expression='debitis',
                data_filter={
                    "magnam": 'doloremque',
                    "accusamus": 'quod',
                    "sunt": 'voluptas',
                },
                name='Cameron Wehner',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='rerum',
            color_palette=17548,
            type='nam',
        ),
        single_value=shared.SingleValue(
            color='ullam',
            decimals=191571,
            label='eos',
            prefix='id',
            suffix='modi',
            type='illum',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    235567,
                    443098,
                    758184,
                ],
            ),
            type='cum',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='culpa',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=637037,
        total_exec_cpu_seconds=955126,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='eius',
                id='52c4842c-9b2a-4d32-9afe-81a88f444457',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=190850,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='saepe',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='quod',
                            field_filter_expr='nulla',
                            fields_=[
                                'quam',
                                'consectetur',
                            ],
                            keep=[
                                'nesciunt',
                                'earum',
                            ],
                            remove=[
                                'dolor',
                                'placeat',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Cynthia Morissette',
                                value='unde',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Orlando Jacobson',
                                value='at',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Ollie Reichert',
                                value='quam',
                            ),
                        ],
                        max_event_bytes=579242,
                        name='Trevor Carter',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='odio',
                            length=518338,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='eos',
                        timestamp_earliest='harum',
                        timestamp_latest='voluptatibus',
                        timestamp_timezone='omnis',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='quos',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='natus',
                            field_filter_expr='aliquam',
                            fields_=[
                                'nisi',
                                'praesentium',
                                'eum',
                                'vitae',
                            ],
                            keep=[
                                'possimus',
                                'libero',
                                'ullam',
                            ],
                            remove=[
                                'maiores',
                                'iste',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Hope Kuhic DDS',
                                value='occaecati',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Terence Leffler',
                                value='veniam',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Jacqueline Prohaska',
                                value='quod',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Ms. Joanne Halvorson',
                                value='illo',
                            ),
                        ],
                        max_event_bytes=954946,
                        name='Nellie Jones',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='nostrum',
                            length=406037,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='voluptate',
                        timestamp_earliest='molestias',
                        timestamp_latest='voluptatibus',
                        timestamp_timezone='ipsum',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='quidem',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='odit',
                            field_filter_expr='molestiae',
                            fields_=[
                                'quia',
                                'inventore',
                                'doloribus',
                                'praesentium',
                            ],
                            keep=[
                                'consequuntur',
                                'laboriosam',
                            ],
                            remove=[
                                'reprehenderit',
                                'soluta',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Lucia Schoen',
                                value='cupiditate',
                            ),
                        ],
                        max_event_bytes=942840,
                        name='Nina Kshlerin',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='ad',
                            length=167613,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='minus',
                        timestamp_earliest='aliquid',
                        timestamp_latest='quam',
                        timestamp_timezone='ea',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='architecto',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='fuga',
                            field_filter_expr='totam',
                            fields_=[
                                'quasi',
                            ],
                            keep=[
                                'officiis',
                            ],
                            remove=[
                                'quae',
                                'dolore',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Mario Runolfsson DDS',
                                value='cumque',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Jesus Corkery',
                                value='facilis',
                            ),
                        ],
                        max_event_bytes=792555,
                        name='Dr. Edmund Mohr',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='est',
                            length=716024,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='nulla',
                        timestamp_earliest='totam',
                        timestamp_latest='praesentium',
                        timestamp_timezone='officiis',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='vitae',
            ),
            shared.EventBreakerRuleset(
                description='delectus',
                id='6c48252d-7771-4e7f-9074-009ef8d29de1',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=813582,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='ducimus',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='aut',
                            field_filter_expr='provident',
                            fields_=[
                                'tempore',
                                'ullam',
                            ],
                            keep=[
                                'mollitia',
                                'ipsa',
                                'quos',
                                'quo',
                            ],
                            remove=[
                                'in',
                                'doloribus',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Erma Kuhic',
                                value='quia',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Ms. Eileen Thompson',
                                value='laborum',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Lamar Schinner',
                                value='illo',
                            ),
                        ],
                        max_event_bytes=584292,
                        name='Suzanne Mante II',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='doloremque',
                            length=738325,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='eius',
                        timestamp_earliest='maiores',
                        timestamp_latest='delectus',
                        timestamp_timezone='quos',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='officiis',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='ab',
                            field_filter_expr='voluptate',
                            fields_=[
                                'itaque',
                            ],
                            keep=[
                                'voluptatem',
                                'dolor',
                                'distinctio',
                                'quaerat',
                            ],
                            remove=[
                                'neque',
                                'nihil',
                                'recusandae',
                                'numquam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Clayton Homenick',
                                value='enim',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Cora Jenkins',
                                value='nesciunt',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Lynda Padberg',
                                value='porro',
                            ),
                        ],
                        max_event_bytes=734292,
                        name='Ella Lang',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='expedita',
                            length=447878,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='delectus',
                        timestamp_earliest='blanditiis',
                        timestamp_latest='minus',
                        timestamp_timezone='tenetur',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='exercitationem',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='a',
                            field_filter_expr='tempore',
                            fields_=[
                                'earum',
                                'occaecati',
                            ],
                            keep=[
                                'quidem',
                            ],
                            remove=[
                                'laborum',
                                'molestias',
                                'a',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Mabel Greenfelder',
                                value='aspernatur',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Ms. Stanley Doyle',
                                value='soluta',
                            ),
                        ],
                        max_event_bytes=15205,
                        name='Grace Kerluke',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='voluptates',
                            length=467109,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='eligendi',
                        timestamp_earliest='fuga',
                        timestamp_latest='consequatur',
                        timestamp_timezone='sit',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                    shared.EventBreakerRulesetRules(
                        condition='earum',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='quis',
                            field_filter_expr='dolorem',
                            fields_=[
                                'sed',
                                'quo',
                                'et',
                            ],
                            keep=[
                                'est',
                            ],
                            remove=[
                                'veniam',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Felipe Wunsch DVM',
                                value='excepturi',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Jamie Collins',
                                value='at',
                            ),
                            shared.EventBreakerRulesetRulesFields(
                                name='Neal McLaughlin',
                                value='soluta',
                            ),
                        ],
                        max_event_bytes=939096,
                        name='Mr. Roy Conn',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='ad',
                            length=244990,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='provident',
                        timestamp_earliest='possimus',
                        timestamp_latest='iste',
                        timestamp_timezone='blanditiis',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                ],
                tags='totam',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=489225,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'iusto',
            'culpa',
            'voluptate',
            'cupiditate',
        ],
    ),
    group='maxime',
    id='d72cd248-4da2-4172-9f2a-c41ef5725f11',
    latest_epoch=432597,
    num_events_after=572996,
    num_events_before=659804,
    query='nobis',
    sample_rate=94487,
    search_config=shared.SearchConfig(
        datasets=[
            'aliquam',
            'vitae',
            'temporibus',
            'voluptatum',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'aspernatur',
            'neque',
            'impedit',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='neque',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='labore',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='quibusdam',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='quaerat',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='perspiciatis',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='iure',
            name='Clay Monahan',
            type=shared.SearchParameterType.STRING,
        ),
        shared.SearchParameter(
            default_value='ipsam',
            name='Ms. Dixie Turner Sr.',
            type=shared.SearchParameterType.STRING,
        ),
        shared.SearchParameter(
            default_value='perspiciatis',
            name='Alfredo Halvorson',
            type=shared.SearchParameterType.NUMBER,
        ),
        shared.SearchParameter(
            default_value='reiciendis',
            name='Pauline Ferry',
            type=shared.SearchParameterType.NUMBER,
        ),
    ],
    search_parameter_values='dolore',
    status=shared.SearchJobStatus.RUNNING,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='dolor',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='perspiciatis',
            precision='accusamus',
            prefix='voluptates',
            suffix='quia',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='aspernatur',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='ut',
        ),
        row_number_column_width=250742,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    target_event_time=37044,
    time_completed=273638,
    time_created=302228,
    time_started=210710,
    type=shared.SearchJobType.SCHEDULED,
    user='impedit',
))

if res.search_job is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | Unique ID                                                      |
| `search_job`                                                   | [Optional[shared.SearchJob]](../../models/shared/searchjob.md) | :heavy_minus_sign:                                             | SearchJob object to be updated                                 |


### Response

**[operations.UpdateSearchJobResponse](../../models/operations/updatesearchjobresponse.md)**

