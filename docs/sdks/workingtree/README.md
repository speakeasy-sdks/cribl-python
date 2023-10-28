# WorkingTree
(*working_tree*)

### Available Operations

* [get](#get) - get the the working tree status

## get

get the the working tree status

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.working_tree.get(group='string')

if res.git_status_results is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group`            | *Optional[str]*    | :heavy_minus_sign: | Group ID           |


### Response

**[operations.GetWorkingTreeResponse](../../models/operations/getworkingtreeresponse.md)**

