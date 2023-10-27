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
    bearer_auth="",
)

req = shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            y_axis=[
                'string',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                data=[
                    {
                        "key": 'string',
                    },
                ],
                data_expression='string',
                data_filter={
                    "key": 'string',
                },
                name='string',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color_palette=486589,
            type='string',
        ),
        single_value=shared.SingleValue(),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    489382,
                ],
            ),
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(),
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=638424,
        total_exec_cpu_seconds=859213,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    shared.EventBreakerRulesetRules(
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            fields_=[
                                'string',
                            ],
                            keep=[
                                'string',
                            ],
                            remove=[
                                'string',
                            ],
                        ),
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                value='string',
                            ),
                        ],
                        name='string',
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(),
                    ),
                ],
            ),
        ],
        disable_breakers=False,
    ),
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'string',
        ],
    ),
    group='string',
    id='<ID>',
    query='string',
    search_config=shared.SearchConfig(
        datasets=[
            'string',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'string',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='string',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='string',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            name='string',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    status=shared.SearchJobStatus.CANCELED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='string',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='string',
            precision='string',
            prefix='string',
            suffix='string',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='string',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='string',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    time_created=996706,
    user='Peyton_Hodkiewicz0',
)

res = s.search_job.create(req)

if res.search_job is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.search_job.delete(id='string')

if res.search_job is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.search_job.get(id='string')

if res.search_job is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.search_job.update(id='string', search_job=shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            y_axis=[
                'string',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                data=[
                    {
                        "key": 'string',
                    },
                ],
                data_expression='string',
                data_filter={
                    "key": 'string',
                },
                name='string',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color_palette=857478,
            type='string',
        ),
        single_value=shared.SingleValue(),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    24555,
                ],
            ),
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(),
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=597129,
        total_exec_cpu_seconds=15652,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    shared.EventBreakerRulesetRules(
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            fields_=[
                                'string',
                            ],
                            keep=[
                                'string',
                            ],
                            remove=[
                                'string',
                            ],
                        ),
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                value='string',
                            ),
                        ],
                        name='string',
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(),
                    ),
                ],
            ),
        ],
        disable_breakers=False,
    ),
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'string',
        ],
    ),
    group='string',
    id='<ID>',
    query='string',
    search_config=shared.SearchConfig(
        datasets=[
            'string',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'string',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='string',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='string',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            name='string',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    status=shared.SearchJobStatus.RUNNING,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='string',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='string',
            precision='string',
            prefix='string',
            suffix='string',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='string',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='string',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    time_created=684199,
    user='Jeffry.Kihn5',
))

if res.search_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | Unique ID                                                      |
| `search_job`                                                   | [Optional[shared.SearchJob]](../../models/shared/searchjob.md) | :heavy_minus_sign:                                             | SearchJob object to be updated                                 |


### Response

**[operations.UpdateSearchJobResponse](../../models/operations/updatesearchjobresponse.md)**

