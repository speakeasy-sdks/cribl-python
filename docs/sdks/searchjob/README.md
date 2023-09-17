# SearchJob

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
            x_axis='possimus',
            y_axis=[
                'neque',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='pariatur',
                data=[
                    {
                        "vel": 'sapiente',
                    },
                ],
                data_expression='mollitia',
                data_filter={
                    "quae": 'quos',
                },
                name='Ellen Veum',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='quisquam',
            color_palette=557987,
            type='consequuntur',
        ),
        single_value=shared.SingleValue(
            color='maiores',
            decimals=81581,
            label='aliquid',
            prefix='laudantium',
            suffix='est',
            type='dolor',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    400879,
                ],
            ),
            type='consectetur',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='cumque',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=525917,
        total_exec_cpu_seconds=527715,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='ducimus',
                id='3e484380-b1f6-4b8c-a275-a60a04c495cc',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=378403,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='occaecati',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='unde',
                            field_filter_expr='illo',
                            fields_=[
                                'nihil',
                            ],
                            keep=[
                                'inventore',
                            ],
                            remove=[
                                'libero',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Miss Joyce Runolfsson',
                                value='facilis',
                            ),
                        ],
                        max_event_bytes=105372,
                        name='Toby Grant',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='rem',
                            length=543353,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='cum',
                        timestamp_earliest='pariatur',
                        timestamp_latest='sapiente',
                        timestamp_timezone='quo',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON,
                    ),
                ],
                tags='quod',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=793282,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'porro',
        ],
    ),
    group='id',
    id='99bc7fc0-b2dc-4e10-873e-42b006d67887',
    latest_epoch=540048,
    num_events_after=697994,
    num_events_before=645544,
    query='atque',
    sample_rate=344856,
    search_config=shared.SearchConfig(
        datasets=[
            'atque',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'architecto',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='est',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='rem',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='quae',
            name='Clark Hamill',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    search_parameter_values='delectus',
    status=shared.SearchJobStatus.FAILED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='natus',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='cumque',
            precision='natus',
            prefix='quaerat',
            suffix='doloribus',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='quia',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='officiis',
        ),
        row_number_column_width=651467,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=337081,
    time_completed=313590,
    time_created=430235,
    time_started=365539,
    type=shared.SearchJobType.SCHEDULED,
    user='nesciunt',
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


res = s.search_job.delete(id='sit')

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


res = s.search_job.get(id='odio')

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


res = s.search_job.update(id='minus', search_job=shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            x_axis='asperiores',
            y_axis=[
                'recusandae',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='voluptates',
                data=[
                    {
                        "praesentium": 'dicta',
                    },
                ],
                data_expression='fugit',
                data_filter={
                    "sit": 'aliquid',
                },
                name='Mrs. Louis Lind',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='laborum',
            color_palette=303421,
            type='deserunt',
        ),
        single_value=shared.SingleValue(
            color='modi',
            decimals=122085,
            label='impedit',
            prefix='eius',
            suffix='voluptatum',
            type='ipsa',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    872991,
                ],
            ),
            type='dolorem',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='repellat',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=132305,
        total_exec_cpu_seconds=80284,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='sequi',
                id='2af03102-d514-4f4c-86f1-8bf9621a6a4f',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=493407,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='esse',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='animi',
                            field_filter_expr='laudantium',
                            fields_=[
                                'esse',
                            ],
                            keep=[
                                'eveniet',
                            ],
                            remove=[
                                'earum',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Rochelle Gislason',
                                value='dignissimos',
                            ),
                        ],
                        max_event_bytes=373449,
                        name='Leticia Hyatt',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='ipsum',
                            length=284885,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='architecto',
                        timestamp_earliest='praesentium',
                        timestamp_latest='eveniet',
                        timestamp_timezone='dolor',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                ],
                tags='libero',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=615277,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'illo',
        ],
    ),
    group='minus',
    id='8d975e0e-8419-4d8f-84f1-44f3e07edcc4',
    latest_epoch=677895,
    num_events_after=644827,
    num_events_before=319834,
    query='reiciendis',
    sample_rate=196451,
    search_config=shared.SearchConfig(
        datasets=[
            'porro',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'laborum',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='nobis',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='omnis',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='ipsam',
            name='Kent Kihn',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    search_parameter_values='ad',
    status=shared.SearchJobStatus.COMPLETED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='molestiae',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='quia',
            precision='laudantium',
            prefix='sed',
            suffix='odit',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='iusto',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='expedita',
        ),
        row_number_column_width=176935,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=199879,
    time_completed=57909,
    time_created=575139,
    time_started=291389,
    type=shared.SearchJobType.DATATYPE_PREVIEW,
    user='accusantium',
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

