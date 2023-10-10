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
    filter_expr=shared.Expression(
        max_cache=449035,
        cache=shared.Map(
            op=shared.MapOp(),
        ),
        declared_variables=[
            'Producer',
        ],
        is_safe=False,
        modified_expression='iste mealy',
        opt=shared.ExpressionOptions(
            args=[
                'Metrics',
            ],
            ast_traverse_callback=shared.TraverseCallback(),
            partial_eval=shared.PartialEvalRewrite(
                field_filter=shared.PartialEvalFieldFilter(),
                null_obj='Market',
            ),
        ),
        original_expression='Grenada',
        partial_expression='synthesizing',
        referenced_cribl_export=False,
        replace_identifiers_expression='content intelligence array',
        replace_literal_expression='Clothing array Kids',
    ),
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

req = operations.QueryMetricsRequest()

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

