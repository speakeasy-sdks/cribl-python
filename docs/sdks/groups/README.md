# Groups

### Available Operations

* [get](#get) - Get a list of ConfigGroup objects

## get

Get a list of ConfigGroup objects

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.groups.get(fields_='est', product='quidem')

if res.config_groups is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `fields_`                                                                  | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | additional fields to add to results: git.commit, git.localChanges, git.log |
| `product`                                                                  | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | filter to specific product: "stream" or "edge"                             |


### Response

**[operations.GetGroupsResponse](../../models/operations/getgroupsresponse.md)**

