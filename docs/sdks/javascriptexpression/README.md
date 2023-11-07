# JavascriptExpression
(*.javascript_expression*)

### Available Operations

* [post](#post) - Evaluate JavaScript expression

## post

Evaluate JavaScript expression

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.javascript_expression.post()

if res.expr_lib_entries is not None:
    # handle response
    pass
```


### Response

**[operations.PostJavascriptExpressionResponse](../../models/operations/postjavascriptexpressionresponse.md)**

