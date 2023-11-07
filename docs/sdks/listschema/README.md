# ListSchema
(*.list_schema*)

### Available Operations

* [get](#get) - Get a list of Schema objects

## get

Get a list of Schema objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.list_schema.get()

if res.schema_lib_entries is not None:
    # handle response
    pass
```


### Response

**[operations.GetListSchemaResponse](../../models/operations/getlistschemaresponse.md)**

