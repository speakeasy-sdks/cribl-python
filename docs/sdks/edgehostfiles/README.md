# EdgeHostFiles
(*edge_host_files*)

### Available Operations

* [get](#get) - Get details about a file on the edge host.

## get

Get details about a file on the edge host.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.edge_host_files.get()

if res.edge_host_files is not None:
    # handle response
    pass

```


### Response

**[operations.GetEdgeHostFilesResponse](../../models/operations/getedgehostfilesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
