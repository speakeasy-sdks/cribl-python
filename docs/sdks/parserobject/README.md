# parser_object

### Available Operations

* [post](#post) - Create Parser

## post

Create Parser

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = {
    "qui": 'libero',
    "maiores": 'nam',
    "pariatur": 'quod',
}

res = s.parser_object.post(req)

if res.parser_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [dict[str, Any]](../../models//.md)        | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostParserObjectResponse](../../models/operations/postparserobjectresponse.md)**

