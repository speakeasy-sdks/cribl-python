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
            x_axis='bluetooth Extended',
            y_axis=[
                'South',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='silver',
                data=[
                    {
                        "minus": 'abnormally',
                    },
                ],
                data_expression='orange Northwest',
                data_filter={
                    "minus": 'SUV',
                },
                name='Screen mobile',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='olive',
            color_palette=357021,
            type='Fresh',
        ),
        single_value=shared.SingleValue(
            color='red',
            decimals=519028,
            label='Bike',
            prefix='Buckinghamshire functionalities Grocery',
            suffix='Metal',
            type='Direct metrics',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    36521,
                ],
            ),
            type='Interactions Senior Mouse',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='or',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=337966,
        total_exec_cpu_seconds=27619,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='Extended multi-state model',
                id='<ID>',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=550483,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='likewise payment 1080p',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='woman',
                            field_filter_expr='Sausages',
                            fields_=[
                                'lavender',
                            ],
                            keep=[
                                'City',
                            ],
                            remove=[
                                'meanwhile',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Dollar Electronic digital',
                                value='Southwest',
                            ),
                        ],
                        max_event_bytes=982450,
                        name='Pop',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='sexy Country',
                            length=519359,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='Electric',
                        timestamp_earliest='Southeast Toys Electric',
                        timestamp_latest='Lead Wagon telecast',
                        timestamp_timezone='program East Outdoors',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.CSV,
                    ),
                ],
                tags='Progressive Dollar Bronze',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=951781,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'Minivan',
        ],
    ),
    group='Bacon Tenge male',
    id='<ID>',
    latest_epoch=995852,
    num_events_after=635788,
    num_events_before=823683,
    query='Car Functionality',
    sample_rate=284120,
    search_config=shared.SearchConfig(
        datasets=[
            'Minivan',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'compressing',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='FTM',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='Oganesson Gasoline',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='Oro',
            name='Extended phew array',
            type=shared.SearchParameterType.NUMBER,
        ),
    ],
    search_parameter_values='South',
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='benchmark',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='tesla',
            precision='Soft',
            prefix='parse',
            suffix='Tasty',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='ducks',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='deposit',
        ),
        row_number_column_width=596806,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=224806,
    time_completed=791070,
    time_created=88424,
    time_started=741384,
    type=shared.SearchJobType.DATATYPE_PREVIEW,
    user='Travis_Rempel93',
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


res = s.search_job.delete(id='program')

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


res = s.search_job.get(id='female')

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


res = s.search_job.update(id='Van', search_job=shared.SearchJob(
    chart_config=shared.ChartConfig(
        axis=shared.ChartConfigAxis(
            x_axis='Reactive',
            y_axis=[
                'dock',
            ],
        ),
        legend=shared.Legend(),
        series=[
            shared.ChartSeries(
                color='orchid',
                data=[
                    {
                        "fuga": 'redundant',
                    },
                ],
                data_expression='Arizona Cotton extend',
                data_filter={
                    "non": 'bifurcated',
                },
                name='silver immediately',
                type=shared.ChartType(),
            ),
        ],
        settings=shared.Settings(
            color='orange',
            color_palette=11873,
            type='Baht Quality',
        ),
        single_value=shared.SingleValue(
            color='lavender',
            decimals=404265,
            label='Galveston pascal',
            prefix='Division Northeast Wooden',
            suffix='Jaguar Dodge',
            type='Buckinghamshire frictionless haptic',
        ),
        x_axis=shared.Axis(
            axis_label=shared.AxisLabel(
                formatter=shared.AxisLabelFormatter(),
                formatter_data=[
                    973871,
                ],
            ),
            type='Kia Turkish',
        ),
    ),
    compatibility_checks=shared.SearchJobCompatibilityChecks(
        datatypes=False,
    ),
    correlation_id='Greens',
    cpu_metrics=shared.CPUTimeMetric(
        total_cpu_seconds=656776,
        total_exec_cpu_seconds=555894,
    ),
    datatype_overrides=shared.DatatypeOverrides(
        breaker_rulesets=[
            shared.EventBreakerRuleset(
                description='Cross-group content-based methodology',
                id='<ID>',
                lib=shared.EventBreakerRulesetLibrary.CUSTOM,
                min_raw_length=992010,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='West',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='Southeast',
                            field_filter_expr='Pickup Ergonomic Money',
                            fields_=[
                                'male',
                            ],
                            keep=[
                                'Account',
                            ],
                            remove=[
                                'Latvian',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='Chips Omnigender tremendously',
                                value='Specialist Bacon Legacy',
                            ),
                        ],
                        max_event_bytes=84221,
                        name='encompassing',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='Consultant',
                            length=175843,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='South',
                        timestamp_earliest='Arab Metal',
                        timestamp_latest='primary surprisingly',
                        timestamp_timezone='calculating models',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                ],
                tags='Pants',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=958003,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'RSS',
        ],
    ),
    group='Jewelery violet',
    id='<ID>',
    latest_epoch=951460,
    num_events_after=947714,
    num_events_before=412253,
    query='orange redundant',
    sample_rate=792088,
    search_config=shared.SearchConfig(
        datasets=[
            'leverage',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'Dynamic',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='asynchronous',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='Global Oriental',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='connect',
            name='killer Manat',
            type=shared.SearchParameterType.BOOLEAN,
        ),
    ],
    search_parameter_values='Ghana',
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='Charlottesville',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='likewise',
            precision='Southwest',
            prefix='optical',
            suffix='drive',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='Hermaphrodite',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='Division',
        ),
        row_number_column_width=403840,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    target_event_time=6983,
    time_completed=20664,
    time_created=770244,
    time_started=519955,
    type=shared.SearchJobType.STANDARD,
    user='Mina5',
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

