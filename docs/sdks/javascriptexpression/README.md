# JavascriptExpression
(*javascript_expression*)

### Available Operations

* [post](#post) - Evaluate JavaScript expression

## post

Evaluate JavaScript expression

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.javascript_expression.post()

if res.expr_lib_entries is not None:
    # handle response
    pass

```


### Response

**[operations.PostJavascriptExpressionResponse](../../models/operations/postjavascriptexpressionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
