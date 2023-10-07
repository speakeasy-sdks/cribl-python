# DatasetObjects
(*dataset_objects*)

### Available Operations

* [get](#get) - Get a list of Dataset objects

## get

Get a list of Dataset objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.dataset_objects.get()

if res.datasets is not None:
    # handle response
```


### Response

**[operations.GetDatasetObjectsResponse](../../models/operations/getdatasetobjectsresponse.md)**

