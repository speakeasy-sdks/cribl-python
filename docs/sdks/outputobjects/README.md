# OutputObjects
(*output_objects*)

### Available Operations

* [get](#get) - Get a list of Output objects

## get

Get a list of Output objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.output_objects.get()

if res.outputs is not None:
    # handle response
    pass

```


### Response

**[operations.GetOutputObjectsResponse](../../models/operations/getoutputobjectsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
