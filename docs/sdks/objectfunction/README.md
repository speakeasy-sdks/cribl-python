# ObjectFunction
(*.object_function*)

### Available Operations

* [get](#get) - Get a list of Function objects

## get

Get a list of Function objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.object_function.get()

if res.functions is not None:
    # handle response
    pass
```


### Response

**[operations.GetObjectFunctionResponse](../../models/operations/getobjectfunctionresponse.md)**

