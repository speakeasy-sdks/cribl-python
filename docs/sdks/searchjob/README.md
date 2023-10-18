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
                data_expression='blue',
                data_filter={
                    "shred": 'abnormally',
                },
                name='deposit',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color_palette=301510,
            type='Northwest',
        ),
        single_value=shared.SingleValue(),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    792620,
                ],
            ),
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(),
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=855952,
        total_exec_cpu_seconds=816588,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    shared.EventBreakerRulesetRules(
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            fields_=[
                                'quantify',
                            ],
                            keep=[
                                'Polestar',
                            ],
                            remove=[
                                'mobile',
                            ],
                        ),
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                value='National',
                            ),
                        ],
                        name='Durham',
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
            'after',
        ],
    ),
    group='overriding',
    id='<ID>',
    query='Bike',
    search_config=shared.SearchConfig(
        datasets=[
            'female',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'Fiat',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='easily',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='Borders',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            name='Profound',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    status=shared.SearchJobStatus.COMPLETED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='animated',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='Minivan',
            precision='though',
            prefix='East',
            suffix='red',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='or',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='Towels',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    time_created=425694,
    user='Izabella_Ritchie',
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
                data_expression='cheater',
                data_filter={
                    "Islands": 'online',
                },
                name='dynamic',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color_palette=788440,
            type='Plastic',
        ),
        single_value=shared.SingleValue(),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    139579,
                ],
            ),
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(),
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=644713,
        total_exec_cpu_seconds=789275,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    shared.EventBreakerRulesetRules(
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            fields_=[
                                'syndicate',
                            ],
                            keep=[
                                'East',
                            ],
                            remove=[
                                'Baht',
                            ],
                        ),
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                value='Quality',
                            ),
                        ],
                        name='guestbook',
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
            'driver',
        ],
    ),
    group='users',
    id='<ID>',
    query='Sharable',
    search_config=shared.SearchConfig(
        datasets=[
            'Division',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'Northeast',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='Wooden',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='Jaguar',
                null_position=shared.SortByFieldNullPosition.NULLS_LAST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            name='visionary',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    status=shared.SearchJobStatus.CANCELED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='frictionless',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='haptic',
            precision='modulo',
            prefix='Kia',
            suffix='Turkish',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='Avon',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='Ranch',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    time_created=119053,
    user='Dejah.Monahan8',
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

