# stage_distributed_package

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

req = operations.PostStageDistributedPackageRequest(
    group='rerum',
    upgrade_percentage='neque',
)

res = s.stage_distributed_package.post(req)

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostStageDistributedPackageRequest](../../models/operations/poststagedistributedpackagerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PostStageDistributedPackageResponse](../../models/operations/poststagedistributedpackageresponse.md)**

