# KeyMetadataEntities
(*key_metadata_entities*)

### Available Operations

* [get](#get) - Get a list of KeyMetadataEntity objects

## get

Get a list of KeyMetadataEntity objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.key_metadata_entities.get()

if res.key_metadata_entities is not None:
    # handle response
    pass
```


### Response

**[operations.GetKeyMetadataEntitiesResponse](../../models/operations/getkeymetadataentitiesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
