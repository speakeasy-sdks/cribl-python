# SearchJob
(*search_job*)

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
            x_axis='voluptas',
            y_axis=[
                'consequuntur',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='officia',
                data=[
                    {
                        "reprehenderit": 'distinctio',
                    },
                ],
                data_expression='eius',
                data_filter={
                    "ipsa": 'rem',
                },
                name='Steven Harris',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='facere',
            color_palette=307173,
            type='quos',
        ),
        single_value=shared.SingleValue(
            color='doloribus',
            decimals=851809,
            label='est',
            prefix='delectus',
            suffix='velit',
            type='vitae',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    201096,
                ],
            ),
            type='similique',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='illo',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=997995,
        total_exec_cpu_seconds=363214,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='doloribus',
                id='d94259c0-b36f-425e-a944-f3b756c11f6c',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=221218,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='ducimus',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='fuga',
                            field_filter_expr='minima',
                            fields_=[
                                'architecto',
                            ],
                            keep=[
                                'qui',
                            ],
                            remove=[
                                'aliquid',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Amber Fisher',
                                value='exercitationem',
                            ),
                        ],
                        max_event_bytes=709701,
                        name='Rodolfo Bailey',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='consequuntur',
                            length=230571,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='modi',
                        timestamp_earliest='veniam',
                        timestamp_latest='quod',
                        timestamp_timezone='itaque',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                    ),
                ],
                tags='quisquam',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=316550,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'doloribus',
        ],
    ),
    group='assumenda',
    id='e10a0ce2-169e-4510-819c-6dc5e3476279',
    latest_epoch=588152,
    num_events_after=739508,
    num_events_before=983854,
    query='facilis',
    sample_rate=697330,
    search_config=shared.SearchConfig(
        datasets=[
            'itaque',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'laboriosam',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='unde',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='perspiciatis',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='cum',
            name='Juana Reichel',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    search_parameter_values='id',
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='autem',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='quo',
            precision='nesciunt',
            prefix='illum',
            suffix='nemo',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='illum',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='facilis',
        ),
        row_number_column_width=247618,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=827051,
    time_completed=927977,
    time_created=718981,
    time_started=866861,
    type=shared.SearchJobType.STANDARD,
    user='facere',
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


res = s.search_job.delete(id='laborum')

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


res = s.search_job.get(id='eveniet')

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


res = s.search_job.update(id='laborum', search_job=shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            x_axis='incidunt',
            y_axis=[
                'maxime',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='ipsam',
                data=[
                    {
                        "alias": 'suscipit',
                    },
                ],
                data_expression='deserunt',
                data_filter={
                    "molestias": 'laborum',
                },
                name='Sergio Grant Sr.',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='aliquid',
            color_palette=301309,
            type='quaerat',
        ),
        single_value=shared.SingleValue(
            color='eligendi',
            decimals=942185,
            label='nostrum',
            prefix='officiis',
            suffix='unde',
            type='nulla',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    621393,
                ],
            ),
            type='mollitia',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='magnam',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=344289,
        total_exec_cpu_seconds=460909,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='corrupti',
                id='adc1ac60-0dec-4001-ac80-2e2ec09ff8f0',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=992667,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='rem',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='dicta',
                            field_filter_expr='suscipit',
                            fields_=[
                                'earum',
                            ],
                            keep=[
                                'doloribus',
                            ],
                            remove=[
                                'velit',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Joy King I',
                                value='vero',
                            ),
                        ],
                        max_event_bytes=566312,
                        name='Mrs. Phyllis Russel Sr.',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='corporis',
                            length=701441,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='error',
                        timestamp_earliest='vel',
                        timestamp_latest='accusantium',
                        timestamp_timezone='id',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='ex',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=555679,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'veritatis',
        ],
    ),
    group='ullam',
    id='1a472af9-23c5-4949-b83f-350cf876ffb9',
    latest_epoch=34245,
    num_events_after=118917,
    num_events_before=795546,
    query='commodi',
    sample_rate=908734,
    search_config=shared.SearchConfig(
        datasets=[
            'porro',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'tempore',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='quidem',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='voluptates',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='eius',
            name='Marianne Zemlak',
            type=shared.SearchParameterType.NUMBER,
        ),
    ],
    search_parameter_values='repellat',
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='animi',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='maiores',
            precision='itaque',
            prefix='nulla',
            suffix='deserunt',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='corporis',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='velit',
        ),
        row_number_column_width=887701,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    target_event_time=638609,
    time_completed=902979,
    time_created=429997,
    time_started=922094,
    type=shared.SearchJobType.STANDARD,
    user='officia',
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

