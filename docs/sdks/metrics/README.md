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
    dim_key_filter='nemo',
    dim_value_filter='soluta',
    earliest=726227,
    filter_expr=shared.Expression(
        max_cache=526907,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'dolorum',
        ],
        is_safe=False,
        modified_expression='odio',
        opt=shared.ExpressionOptions(
            allow_internal=False,
            args=[
                'fugit',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            context='alias',
            disallow_assign=False,
            max_num_of_allowed_iterations=168042,
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='vel',
            ),
            replace_identifiers=False,
            replace_literals=False,
            unprotected=False,
        ),
        original_expression='quae',
        partial_expression='quae',
        referenced_cribl_export=False,
        replace_identifiers_expression='modi',
        replace_literal_expression='neque',
    ),
    max_values=348357,
    metric_name_filter='itaque',
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
    earliest=88248,
    filter_expr='ipsum',
    latest=602229,
    metric_name_filter='nulla',
    num_buckets=714376,
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

