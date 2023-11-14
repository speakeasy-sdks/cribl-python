# Packs
(*packs*)

### Available Operations

* [get](#get) - Get info on packs

## get

Get info on packs

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.packs.get()

if res.pack_infos is not None:
    # handle response
    pass
```


### Response

**[operations.GetPacksResponse](../../models/operations/getpacksresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
