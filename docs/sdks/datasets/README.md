# Datasets
(*datasets*)

### Available Operations

* [get](#get) - Get a list of DatasetProviderType objects

## get

Get a list of DatasetProviderType objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.datasets.get()

if res.dataset_provider_types is not None:
    # handle response
```


### Response

**[operations.GetDatasetProviderTypesResponse](../../models/operations/getdatasetprovidertypesresponse.md)**

