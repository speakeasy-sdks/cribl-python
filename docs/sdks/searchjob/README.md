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
            x_axis='nihil',
            y_axis=[
                'ad',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='nisi',
                data=[
                    {
                        "tenetur": 'quis',
                    },
                ],
                data_expression='quibusdam',
                data_filter={
                    "nemo": 'suscipit',
                },
                name='Paul Powlowski MD',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='sapiente',
            color_palette=152364,
            type='possimus',
        ),
        single_value=shared.SingleValue(
            color='repellat',
            decimals=921060,
            label='architecto',
            prefix='adipisci',
            suffix='pariatur',
            type='harum',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    294266,
                ],
            ),
            type='voluptatibus',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='iure',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=127087,
        total_exec_cpu_seconds=795457,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='soluta',
                id='a3f8941a-ebc0-4b80-a692-4d3b2ecfcc8f',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=532326,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='iste',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='corporis',
                            field_filter_expr='accusantium',
                            fields_=[
                                'illo',
                            ],
                            keep=[
                                'aut',
                            ],
                            remove=[
                                'doloribus',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Lynette Senger',
                                value='vel',
                            ),
                        ],
                        max_event_bytes=960813,
                        name='Mrs. Eric Lueilwitz',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='ad',
                            length=305047,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='quas',
                        timestamp_earliest='consequuntur',
                        timestamp_latest='maiores',
                        timestamp_timezone='inventore',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.JSON_ARRAY,
                    ),
                ],
                tags='laudantium',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=665872,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'dolor',
        ],
    ),
    group='aliquid',
    id='3c8873e4-8438-40b1-b6b8-ca275a60a04c',
    latest_epoch=303292,
    num_events_after=613702,
    num_events_before=355889,
    query='eligendi',
    sample_rate=810302,
    search_config=shared.SearchConfig(
        datasets=[
            'voluptas',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'occaecati',
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
                field_name='nihil',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='libero',
            name='Miss Joyce Runolfsson',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    search_parameter_values='beatae',
    status=shared.SearchJobStatus.CANCELED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='delectus',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='labore',
            precision='expedita',
            prefix='corrupti',
            suffix='rem',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='atque',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='officiis',
        ),
        row_number_column_width=739633,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=956871,
    time_completed=775427,
    time_created=277990,
    time_started=797293,
    type=shared.SearchJobType.SCHEDULED,
    user='porro',
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


res = s.search_job.delete(id='id')

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


res = s.search_job.get(id='excepturi')

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


res = s.search_job.update(id='occaecati', search_job=shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            x_axis='libero',
            y_axis=[
                'quo',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='esse',
                data=[
                    {
                        "hic": 'maxime',
                    },
                ],
                data_expression='accusantium',
                data_filter={
                    "soluta": 'fugit',
                },
                name='Mr. Guillermo Walter',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='iusto',
            color_palette=219860,
            type='voluptates',
        ),
        single_value=shared.SingleValue(
            color='tempora',
            decimals=169935,
            label='rerum',
            prefix='doloremque',
            suffix='voluptatem',
            type='eum',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    873320,
                ],
            ),
            type='eum',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='reprehenderit',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=531195,
        total_exec_cpu_seconds=502393,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='nihil',
                id='8ba8581a-5820-48c5-8fef-a9c95f2eac55',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=430235,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='nemo',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='illum',
                            field_filter_expr='nesciunt',
                            fields_=[
                                'sit',
                            ],
                            keep=[
                                'odio',
                            ],
                            remove=[
                                'minus',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Rolando Veum Sr.',
                                value='sit',
                            ),
                        ],
                        max_event_bytes=396234,
                        name='Mrs. Louis Lind',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='laborum',
                            length=303421,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.FORMAT,
                        ),
                        timestamp_anchor_regex='modi',
                        timestamp_earliest='sunt',
                        timestamp_latest='impedit',
                        timestamp_timezone='eius',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                ],
                tags='ipsa',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=872991,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'dolorem',
        ],
    ),
    group='repellat',
    id='2132af03-102d-4514-b4cc-6f18bf9621a6',
    latest_epoch=657301,
    num_events_after=296128,
    num_events_before=945419,
    query='dignissimos',
    sample_rate=457835,
    search_config=shared.SearchConfig(
        datasets=[
            'animi',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'laudantium',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='esse',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='earum',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='officiis',
            name='Susie Ward',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    search_parameter_values='impedit',
    status=shared.SearchJobStatus.COMPLETED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='quis',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='facilis',
            precision='ipsum',
            prefix='ut',
            suffix='quaerat',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='architecto',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='praesentium',
        ),
        row_number_column_width=907899,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    target_event_time=709051,
    time_completed=730003,
    time_created=615277,
    time_started=74921,
    type=shared.SearchJobType.SCHEDULED,
    user='quos',
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

