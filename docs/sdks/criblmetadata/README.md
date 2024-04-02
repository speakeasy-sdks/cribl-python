# CriblMetadata
(*cribl_metadata*)

### Available Operations

* [get](#get) - Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

## get

Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.cribl_metadata.get()

if res.res is not None:
    # handle response
    pass

```


### Response

**[operations.GetCriblMetadataResponse](../../models/operations/getcriblmetadataresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
