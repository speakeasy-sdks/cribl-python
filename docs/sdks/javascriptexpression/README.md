# JavascriptExpression

### Available Operations

* [post](#post) - Evaluate JavaScript expression

## post

Evaluate JavaScript expression

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.javascript_expression.post()

if res.expr_lib_entries is not None:
    # handle response
```


### Response

**[operations.PostJavascriptExpressionResponse](../../models/operations/postjavascriptexpressionresponse.md)**

