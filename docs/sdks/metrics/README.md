# Metrics
(*metrics*)

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
    dim_key_filter='payment',
    dim_value_filter='Silver',
    earliest=562272,
    filter_expr=shared.Expression(
        max_cache=614946,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'mealy',
        ],
        is_safe=False,
        modified_expression='off',
        opt=shared.ExpressionOptions(
            allow_internal=False,
            args=[
                'beside',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            context='Arizona synthesizing',
            disallow_assign=False,
            max_num_of_allowed_iterations=767148,
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='withdrawal',
            ),
            replace_identifiers=False,
            replace_literals=False,
            unprotected=False,
        ),
        original_expression='intelligence',
        partial_expression='applications Clothing',
        referenced_cribl_export=False,
        replace_identifiers_expression='Distributed Intranet',
        replace_literal_expression='Recycled secondary',
    ),
    max_values=800849,
    metric_name_filter='down',
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
    earliest=764604,
    filter_expr='swoosh Colombia Coupe',
    latest=636850,
    metric_name_filter='up Shoes Fresh',
    num_buckets=359592,
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

