# ParserID
(*parser_id*)

### Available Operations

* [delete](#delete) - Delete Parser
* [get](#get) - Get Parser by ID
* [update](#update) - Update Parser

## delete

Delete Parser

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.parser_id.delete(id='string')

if res.parser_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteParserIDResponse](../../models/operations/deleteparseridresponse.md)**


## get

Get Parser by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.parser_id.get(id='string')

if res.parser_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetParserIDResponse](../../models/operations/getparseridresponse.md)**


## update

Update Parser

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.parser_id.update(id='string', parser_lib_entry=shared.ParserLibEntry(
    additional_properties={
        "key": 'string',
    },
    id='<ID>',
))

if res.parser_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique ID                                                                |
| `parser_lib_entry`                                                       | [Optional[shared.ParserLibEntry]](../../models/shared/parserlibentry.md) | :heavy_minus_sign:                                                       | Parser object to be updated                                              |


### Response

**[operations.UpdateParserIDResponse](../../models/operations/updateparseridresponse.md)**

