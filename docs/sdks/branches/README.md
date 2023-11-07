# Branches
(*.branches*)

### Available Operations

* [get](#get) - get the list of branches

## get

get the list of branches

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.branches.get()

if res.branches is not None:
    # handle response
    pass
```


### Response

**[operations.GetBranchesResponse](../../models/operations/getbranchesresponse.md)**

