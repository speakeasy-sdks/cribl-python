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
                'online',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                data=[
                    {
                        "Configuration": 'Money',
                    },
                ],
                data_expression='Cambridgeshire grey technology',
                data_filter={
                    "East": 'orange',
                },
                name='male',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color_palette=855952,
            type='quantify Polestar mobile',
        ),
        single_value=shared.SingleValue(),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    656256,
                ],
            ),
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(),
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=357021,
        total_exec_cpu_seconds=28548,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    shared.EventBreakerRulesetRules(
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            fields_=[
                                'Fresh',
                            ],
                            keep=[
                                'South',
                            ],
                            remove=[
                                'Intelligent',
                            ],
                        ),
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                value='female',
                            ),
                        ],
                        name='functionalities Grocery Borders',
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
            'Northwest',
        ],
    ),
    group='Kentucky animated',
    id='<ID>',
    query='Interactions Senior Mouse',
    search_config=shared.SearchConfig(
        datasets=[
            'West',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'array',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='Towels',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='payment 1080p',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            name='silver Indiana',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='mmm',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='lavender',
            precision='City',
            prefix='meanwhile',
            suffix='incompatible',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='overhang',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='Electronic',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    time_created=176548,
    user='Eric_Bode4',
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


res = s.search_job.delete(id='program')

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


res = s.search_job.get(id='female')

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


res = s.search_job.update(id='Van', search_job=shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            y_axis=[
                'East',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                data=[
                    {
                        "male": 'Metal',
                    },
                ],
                data_expression='Arizona Cotton extend',
                data_filter={
                    "Plastic": 'Carolina',
                },
                name='immediately implement JBOD',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color_palette=771203,
            type='Representative Home',
        ),
        single_value=shared.SingleValue(),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    338819,
                ],
            ),
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(),
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=756247,
        total_exec_cpu_seconds=356752,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    shared.EventBreakerRulesetRules(
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            fields_=[
                                'Gasoline',
                            ],
                            keep=[
                                'Lev',
                            ],
                            remove=[
                                'Wooden',
                            ],
                        ),
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                value='Jaguar Dodge',
                            ),
                        ],
                        name='Buckinghamshire frictionless haptic',
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
            'modulo',
        ],
    ),
    group='navigating Diesel Avon',
    id='<ID>',
    query='hungrily',
    search_config=shared.SearchConfig(
        datasets=[
            'male',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'hack',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='Xenogender',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='ADP',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            name='fuchsia deliverables',
            type=shared.SearchParameterType.NUMBER,
        ),
    ],
    status=shared.SearchJobStatus.RUNNING,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='Money',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='male',
            precision='Account',
            prefix='Latvian',
            suffix='ew',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='global',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='squat',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    time_created=652850,
    user='Sharon_Shields31',
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

