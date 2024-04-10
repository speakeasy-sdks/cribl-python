# Versioning
(*versioning*)

### Available Operations

* [get](#get) - Get info about versioning availability

## get

Get info about versioning availability

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.versioning.get()

if res.git_infos is not None:
    # handle response
    pass

```


### Response

**[operations.GetVersioningResponse](../../models/operations/getversioningresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
