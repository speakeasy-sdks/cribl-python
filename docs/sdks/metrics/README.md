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
    dim_key_filter='similique',
    dim_value_filter='ea',
    earliest=657301,
    filter_expr=shared.Expression(
        max_cache=296128,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'dignissimos',
            'esse',
            'animi',
            'laudantium',
        ],
        is_safe=False,
        modified_expression='esse',
        opt=shared.ExpressionOptions(
            allow_internal=False,
            args=[
                'earum',
                'velit',
                'officiis',
                'eius',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            context='rerum',
            disallow_assign=False,
            max_num_of_allowed_iterations=930111,
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='dignissimos',
            ),
            replace_identifiers=False,
            replace_literals=False,
            unprotected=False,
        ),
        original_expression='ipsam',
        partial_expression='explicabo',
        referenced_cribl_export=False,
        replace_identifiers_expression='impedit',
        replace_literal_expression='aliquid',
    ),
    max_values=339843,
    metric_name_filter='facilis',
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
    earliest=218128,
    filter_expr='ut',
    latest=308819,
    metric_name_filter='architecto',
    num_buckets=506966,
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

