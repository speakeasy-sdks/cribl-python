# metrics

### Available Operations

* [post](#post) - Enumerate all internal system metrics
* [query](#query) - Query raw internal system metrics

## post

Enumerate all internal system metrics

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.GetNamesOpts(
    dim_key_filter='illum',
    dim_value_filter='ea',
    earliest=889201,
    filter_expr=shared.Expression(
        max_cache=96711,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'animi',
            'necessitatibus',
            'voluptatem',
            'maiores',
        ],
        is_safe=False,
        modified_expression='odio',
        opt=shared.ExpressionOptions(
            allow_internal=False,
            args=[
                'fuga',
                'itaque',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            context='possimus',
            disallow_assign=False,
            max_num_of_allowed_iterations=947561,
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='sed',
            ),
            replace_identifiers=False,
            replace_literals=False,
            unprotected=False,
        ),
        original_expression='deserunt',
        partial_expression='eligendi',
        referenced_cribl_export=False,
        replace_identifiers_expression='id',
        replace_literal_expression='distinctio',
    ),
    max_values=358558,
    metric_name_filter='quas',
)

res = s.metrics.post(req)

if res.metrics_info is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.GetNamesOpts](../../models/shared/getnamesopts.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.PostMetricsResponse](../../models/operations/postmetricsresponse.md)**


## query

Query raw internal system metrics

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.QueryMetricsRequest(
    earliest=745304,
    filter_expr='cupiditate',
    latest=602561,
    metric_name_filter='et',
    num_buckets=786319,
)

res = s.metrics.query(req)

if res.metrics_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.QueryMetricsRequest](../../models/operations/querymetricsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.QueryMetricsResponse](../../models/operations/querymetricsresponse.md)**

