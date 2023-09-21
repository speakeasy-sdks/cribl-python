# StageDistributedPackage

### Available Operations

* [post](#post) - Stage distributed group upgrade

## post

Stage distributed group upgrade

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.stage_distributed_package.post(group='aliquam', upgrade_percentage='delectus')

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `group`                                                        | *str*                                                          | :heavy_check_mark:                                             | Group to upgrade                                               |
| `upgrade_percentage`                                           | *Optional[str]*                                                | :heavy_minus_sign:                                             | body number percentage of nodes on the worker group to upgrade |


### Response

**[operations.PostStageDistributedPackageResponse](../../models/operations/poststagedistributedpackageresponse.md)**

