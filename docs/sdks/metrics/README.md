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
    dim_key_filter='voluptatem',
    dim_value_filter='ipsam',
    earliest=425946,
    filter_expr=shared.Expression(
        max_cache=1383,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'quasi',
        ],
        is_safe=False,
        modified_expression='non',
        opt=shared.ExpressionOptions(
            allow_internal=False,
            args=[
                'maiores',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            context='enim',
            disallow_assign=False,
            max_num_of_allowed_iterations=575213,
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='nulla',
            ),
            replace_identifiers=False,
            replace_literals=False,
            unprotected=False,
        ),
        original_expression='deserunt',
        partial_expression='esse',
        referenced_cribl_export=False,
        replace_identifiers_expression='nemo',
        replace_literal_expression='reprehenderit',
    ),
    max_values=667715,
    metric_name_filter='quis',
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
    earliest=571844,
    filter_expr='accusamus',
    latest=774684,
    metric_name_filter='hic',
    num_buckets=900103,
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

