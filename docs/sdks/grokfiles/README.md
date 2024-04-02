# GrokFiles
(*grok_files*)

### Available Operations

* [get](#get) - Get a list of GrokFile objects

## get

Get a list of GrokFile objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.grok_files.get()

if res.grok_files is not None:
    # handle response
    pass

```


### Response

**[operations.GetGrokFilesResponse](../../models/operations/getgrokfilesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
