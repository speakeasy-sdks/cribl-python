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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.SearchJob(
    chart_config=components.ChartConfig(
        axis=components.ChartConfigAxis(
            y_axis=[
                'string',
            ],
        ),
        legend=components.Legend(),
        series=[
            components.ChartSeries(
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
                type=components.ChartType(),
            ),
        ],
        settings=components.Settings(
            color_palette=486589,
            type='string',
        ),
        single_value=components.SingleValue(),
        x_axis=components.Axis(
            axis_label=components.AxisLabel(
                formatter=components.Formatter(),
                formatter_data=[
                    489382,
                ],
            ),
        ),
    ),
    compatibility_checks=components.CompatibilityChecks(),
    cpu_metrics=components.CPUTimeMetric(
        total_cpu_seconds=638424,
        total_exec_cpu_seconds=859213,
    ),
    datatype_overrides=components.DatatypeOverrides(
        breaker_rulesets=[
            components.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    components.EventBreakerRulesetRules(
                        definitions=components.Definitions(
                            fields=[
                                'string',
                            ],
                            keep=[
                                'string',
                            ],
                            remove=[
                                'string',
                            ],
                        ),
                        fields=[
                            components.Fields(
                                value='string',
                            ),
                        ],
                        name='string',
                        timestamp=components.EventBreakerRulesetTimestampFormat(),
                    ),
                ],
            ),
        ],
        disable_breakers=False,
    ),
    error_state_config=components.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'string',
        ],
    ),
    group='string',
    id='<ID>',
    query='string',
    search_config=components.SearchConfig(
        datasets=[
            'string',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'string',
        ],
        search_terms=[
            components.SearchTerm(
                is_case_sensitive=False,
                term='string',
            ),
        ],
        sort_fields=[
            components.SortByField(
                direction=components.Direction.ASCENDING,
                field_name='string',
                null_position=components.NullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        components.SearchParameter(
            name='string',
            type=components.SearchParameterType.STRING,
        ),
    ],
    status=components.SearchJobStatus.CANCELED,
    table_config=components.TableViewSettings(
        column_filter_settings=components.ColumnFilterSettings(
            contains='string',
        ),
        column_format_settings=components.ColumnFormatSettings(
            palette='string',
            precision='string',
            prefix='string',
            suffix='string',
        ),
        column_order_settings=components.ColumnOrderSettings(
            order='string',
        ),
        column_sort_settings=components.ColumnSortSettings(
            sort='string',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=components.ViewMode.EVENT,
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

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.SearchJob](../../models/components/searchjob.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateSearchJobResponse](../../models/operations/createsearchjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## delete

Delete SearchJob

### Example Usage

```python
import cribl
from cribl.models import operations

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get SearchJob by ID

### Example Usage

```python
import cribl
from cribl.models import operations

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update SearchJob

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.search_job.update(id='string', search_job=components.SearchJob(
    chart_config=components.ChartConfig(
        axis=components.ChartConfigAxis(
            y_axis=[
                'string',
            ],
        ),
        legend=components.Legend(),
        series=[
            components.ChartSeries(
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
                type=components.ChartType(),
            ),
        ],
        settings=components.Settings(
            color_palette=857478,
            type='string',
        ),
        single_value=components.SingleValue(),
        x_axis=components.Axis(
            axis_label=components.AxisLabel(
                formatter=components.Formatter(),
                formatter_data=[
                    24555,
                ],
            ),
        ),
    ),
    compatibility_checks=components.CompatibilityChecks(),
    cpu_metrics=components.CPUTimeMetric(
        total_cpu_seconds=597129,
        total_exec_cpu_seconds=15652,
    ),
    datatype_overrides=components.DatatypeOverrides(
        breaker_rulesets=[
            components.EventBreakerRuleset(
                id='<ID>',
                rules=[
                    components.EventBreakerRulesetRules(
                        definitions=components.Definitions(
                            fields=[
                                'string',
                            ],
                            keep=[
                                'string',
                            ],
                            remove=[
                                'string',
                            ],
                        ),
                        fields=[
                            components.Fields(
                                value='string',
                            ),
                        ],
                        name='string',
                        timestamp=components.EventBreakerRulesetTimestampFormat(),
                    ),
                ],
            ),
        ],
        disable_breakers=False,
    ),
    error_state_config=components.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'string',
        ],
    ),
    group='string',
    id='<ID>',
    query='string',
    search_config=components.SearchConfig(
        datasets=[
            'string',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'string',
        ],
        search_terms=[
            components.SearchTerm(
                is_case_sensitive=False,
                term='string',
            ),
        ],
        sort_fields=[
            components.SortByField(
                direction=components.Direction.ASCENDING,
                field_name='string',
                null_position=components.NullPosition.NULLS_LAST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        components.SearchParameter(
            name='string',
            type=components.SearchParameterType.BOOLEAN,
        ),
    ],
    status=components.SearchJobStatus.RUNNING,
    table_config=components.TableViewSettings(
        column_filter_settings=components.ColumnFilterSettings(
            contains='string',
        ),
        column_format_settings=components.ColumnFormatSettings(
            palette='string',
            precision='string',
            prefix='string',
            suffix='string',
        ),
        column_order_settings=components.ColumnOrderSettings(
            order='string',
        ),
        column_sort_settings=components.ColumnSortSettings(
            sort='string',
        ),
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=components.ViewMode.TABLE,
    ),
    time_created=684199,
    user='Jeffry.Kihn5',
))

if res.search_job is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique ID                                                              |
| `search_job`                                                           | [Optional[components.SearchJob]](../../models/components/searchjob.md) | :heavy_minus_sign:                                                     | SearchJob object to be updated                                         |


### Response

**[operations.UpdateSearchJobResponse](../../models/operations/updatesearchjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
