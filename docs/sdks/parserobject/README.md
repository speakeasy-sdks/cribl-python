# ParserObject
(*parser_object*)

### Available Operations

* [post](#post) - Create Parser

## post

Create Parser

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.ParserLibEntry(
    additional_properties={
        'key': 'string',
    },
    id='<ID>',
)

res = s.parser_object.post(req)

if res.parser_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.ParserLibEntry](../../models/components/parserlibentry.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostParserObjectResponse](../../models/operations/postparserobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
