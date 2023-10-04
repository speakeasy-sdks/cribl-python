# ListDataSample
(*list_data_sample*)

### Available Operations

* [get](#get) - Get a list of DataSample objects

## get

Get a list of DataSample objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.list_data_sample.get()

if res.data_samples is not None:
    # handle response
```


### Response

**[operations.GetListDataSampleResponse](../../models/operations/getlistdatasampleresponse.md)**

