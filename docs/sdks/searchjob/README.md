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
                lib='azure Dollar',
                min_raw_length=496323,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='Rubber silver Indiana',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='Toyota Neptunium round',
                            field_filter_expr='Salad',
                            fields_=[
                                'invoice',
                            ],
                            keep=[
                                'Dollar',
                            ],
                            remove=[
                                'Electronic',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='pink Southwest',
                                value='Mongolia Maine sexy',
                            ),
                        ],
                        max_event_bytes=583353,
                        name='overriding networks',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='mole female',
                            length=564156,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.CURRENT,
                        ),
                        timestamp_anchor_regex='readily West',
                        timestamp_earliest='telecast modest aged',
                        timestamp_latest='Outdoors Passenger',
                        timestamp_timezone='Dollar Bronze stockings',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.HEADER,
                    ),
                ],
                tags='Bacon Tenge male',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=995852,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'Creative',
        ],
    ),
    group='Car Functionality',
    id='<ID>',
    latest_epoch=284120,
    num_events_after=841009,
    num_events_before=608384,
    query='Cotton sexy',
    sample_rate=492289,
    search_config=shared.SearchConfig(
        datasets=[
            'Oganesson',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'Gasoline',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='Oro',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.DESCENDING,
                field_name='Soft bandwidth',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='yum',
            name='tesla Soft',
            type=shared.SearchParameterType.NUMBER,
        ),
    ],
    search_parameter_values='demob',
    status=shared.SearchJobStatus.QUEUED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='ducks',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='deposit',
            precision='Latin',
            prefix='Oriental',
            suffix='Northwest',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='Copernicium',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='lux',
        ),
        row_number_column_width=44809,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.EVENT,
    ),
    target_event_time=219271,
    time_completed=78523,
    time_created=508068,
    time_started=721658,
    type=shared.SearchJobType.STANDARD,
    user='Nicholaus.Homenick',
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
                lib='North ADP Southeast',
                min_raw_length=787473,
                rules=[
                    shared.EventBreakerRulesetRules(
                        condition='deliverables Ergonomic Money',
                        definitions=shared.EventBreakerRulesetRulesDefinitions(
                            dst_field='Group wank Latvian',
                            field_filter_expr='Chips Omnigender tremendously',
                            fields_=[
                                'pace',
                            ],
                            keep=[
                                'aggregate',
                            ],
                            remove=[
                                'Benz',
                            ],
                        ),
                        disabled=False,
                        fields_=[
                            shared.EventBreakerRulesetRulesFields(
                                name='port',
                                value='Tools',
                            ),
                        ],
                        max_event_bytes=338673,
                        name='Consultant',
                        parser_enabled=False,
                        timestamp=shared.EventBreakerRulesetRulesTimestampFormat(
                            format='Incredible',
                            length=98386,
                            type=shared.EventBreakerRulesetRulesTimestampFormatTimestampType.AUTO,
                        ),
                        timestamp_anchor_regex='Arab Metal',
                        timestamp_earliest='primary surprisingly',
                        timestamp_latest='calculating models',
                        timestamp_timezone='North RSS Electronic',
                        type=shared.EventBreakerRulesetRulesEventBreakerType.TIMESTAMP,
                    ),
                ],
                tags='Franc',
            ),
        ],
        disable_breakers=False,
    ),
    earliest_epoch=412253,
    error_state_config=shared.SearchJobErrorStateConfig(
        coordinated=False,
        error_messages=[
            'Trans',
        ],
    ),
    group='Auto Baby',
    id='<ID>',
    latest_epoch=237592,
    num_events_after=249026,
    num_events_before=373569,
    query='Fantastic',
    sample_rate=784089,
    search_config=shared.SearchConfig(
        datasets=[
            'leading',
        ],
        has_send_operator=False,
        ordered_field_names=[
            'GB',
        ],
        search_terms=[
            shared.SearchTerm(
                is_case_sensitive=False,
                term='Manat absent',
            ),
        ],
        sort_fields=[
            shared.SortByField(
                direction=shared.SortByFieldDirection.ASCENDING,
                field_name='Charlottesville likewise Southwest',
                null_position=shared.SortByFieldNullPosition.NULLS_FIRST,
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    search_parameter_declarations=[
        shared.SearchParameter(
            default_value='minty',
            name='Division Checking',
            type=shared.SearchParameterType.STRING,
        ),
    ],
    search_parameter_values='Hybrid',
    status=shared.SearchJobStatus.CANCELED,
    table_config=shared.TableViewSettings(
        column_filter_settings=shared.ColumnFilterSettings(
            contains='City',
        ),
        column_format_settings=shared.ColumnFormatSettings(
            palette='Dinar',
            precision='Southwest',
            prefix='synthesizing',
            suffix='Legacy',
        ),
        column_order_settings=shared.ColumnOrderSettings(
            order='mole',
        ),
        column_sort_settings=shared.ColumnSortSettings(
            sort='pish',
        ),
        row_number_column_width=32801,
        show_column_totals=False,
        show_column_totals_pinned=False,
        show_row_numbers=False,
        show_row_totals=False,
        show_row_totals_pinned=False,
        view_mode=shared.TableViewSettingsViewMode.TABLE,
    ),
    target_event_time=316154,
    time_completed=504322,
    time_created=242085,
    time_started=99360,
    type=shared.SearchJobType.SCHEDULED,
    user='Quinn21',
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

