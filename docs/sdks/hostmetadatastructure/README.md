# HostMetadataStructure
(*host_metadata_structure*)

### Available Operations

* [get](#get) - Get the host's metadata structure

## get

Get the host's metadata structure

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.host_metadata_structure.get()

if res.edge_metadatas is not None:
    # handle response
    pass
```


### Response

**[operations.GetHostMetadataStructureResponse](../../models/operations/gethostmetadatastructureresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
