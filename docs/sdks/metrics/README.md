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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.GetNamesOpts(
    filter_expr=components.Expression(
        max_cache=449035,
        cache=components.Map(
            op=components.Op(),
        ),
        declared_variables=[
            'string',
        ],
        is_safe=False,
        modified_expression='string',
        opt=components.ExpressionOptions(
            args=[
                'string',
            ],
            ast_traverse_callback=components.TraverseCallback(),
            partial_eval=components.PartialEvalRewrite(
                field_filter=components.PartialEvalFieldFilter(),
                null_obj='string',
            ),
        ),
        original_expression='string',
        partial_expression='string',
        referenced_cribl_export=False,
        replace_identifiers_expression='string',
        replace_literal_expression='string',
    ),
)

res = s.metrics.post(req)

if res.metrics_info is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.GetNamesOpts](../../models/components/getnamesopts.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostMetricsResponse](../../models/operations/postmetricsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## query

Query raw internal system metrics

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.QueryMetricsRequest()

res = s.metrics.query(req)

if res.metrics_info is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.QueryMetricsRequest](../../models/operations/querymetricsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.QueryMetricsResponse](../../models/operations/querymetricsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
