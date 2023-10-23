# ParserObject
(*parser_object*)

### Available Operations

* [post](#post) - Create Parser

## post

Create Parser

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.ParserLibEntry(
    additional_properties={
        "key": 'string',
    },
    id='<ID>',
)

res = s.parser_object.post(req)

if res.parser_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.ParserLibEntry](../../models/shared/parserlibentry.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostParserObjectResponse](../../models/operations/postparserobjectresponse.md)**

