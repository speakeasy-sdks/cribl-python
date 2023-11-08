# ConfiguredCollectors
(*.configured_collectors*)

### Available Operations

* [get](#get) - Get list of configured collectors

## get

Get list of configured collectors

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.configured_collectors.get()

if res.configured_collectors is not None:
    # handle response
    pass
```


### Response

**[operations.GetConfiguredCollectorsResponse](../../models/operations/getconfiguredcollectorsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
