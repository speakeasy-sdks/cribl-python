# GrokFiles
(*.grok_files*)

### Available Operations

* [get](#get) - Get a list of GrokFile objects

## get

Get a list of GrokFile objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.grok_files.get()

if res.grok_files is not None:
    # handle response
    pass
```


### Response

**[operations.GetGrokFilesResponse](../../models/operations/getgrokfilesresponse.md)**

