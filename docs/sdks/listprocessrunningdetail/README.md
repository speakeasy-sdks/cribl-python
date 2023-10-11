# ListProcessRunningDetail
(*list_process_running_detail*)

### Available Operations

* [get](#get) - Get a detailed list of processes running on the edge host

## get

Get a detailed list of processes running on the edge host

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.list_process_running_detail.get()

if res.processes is not None:
    # handle response
```


### Response

**[operations.GetListProcessRunningDetailResponse](../../models/operations/getlistprocessrunningdetailresponse.md)**

