# SystemInfo
(*.system_info*)

### Available Operations

* [get](#get) - Get basic system information

## get

Get basic system information

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.system_info.get()

if res.system_info_objects is not None:
    # handle response
    pass
```


### Response

**[operations.GetSystemInfoResponse](../../models/operations/getsysteminforesponse.md)**

