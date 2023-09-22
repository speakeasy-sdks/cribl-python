# Metrics

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
    dim_key_filter='inventore',
    dim_value_filter='facere',
    earliest=726878,
    filter_expr=shared.Expression(
        max_cache=102413,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'voluptatibus',
        ],
        is_safe=False,
        modified_expression='quia',
        opt=shared.ExpressionOptions(
            allow_internal=False,
            args=[
                'porro',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            context='aliquam',
            disallow_assign=False,
            max_num_of_allowed_iterations=247045,
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='illo',
            ),
            replace_identifiers=False,
            replace_literals=False,
            unprotected=False,
        ),
        original_expression='accusantium',
        partial_expression='vel',
        referenced_cribl_export=False,
        replace_identifiers_expression='ea',
        replace_literal_expression='beatae',
    ),
    max_values=877751,
    metric_name_filter='excepturi',
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
    earliest=431994,
    filter_expr='velit',
    latest=284086,
    metric_name_filter='perspiciatis',
    num_buckets=935302,
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

