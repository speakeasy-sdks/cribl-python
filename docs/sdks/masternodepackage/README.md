# master_node_package

### Available Operations

* [post](#post) - Upgrade master node with the provided package

## post

Upgrade master node with the provided package

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.UpgradeMasterRequest(
    packages=[
        shared.UpgradeMasterRequestPackages(
            package_hash_url='expedita',
            package_url='hic',
        ),
        shared.UpgradeMasterRequestPackages(
            package_hash_url='excepturi',
            package_url='aliquid',
        ),
        shared.UpgradeMasterRequestPackages(
            package_hash_url='sed',
            package_url='beatae',
        ),
    ],
)

res = s.master_node_package.post(req)

if res.cribl is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.UpgradeMasterRequest](../../models/shared/upgrademasterrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostMasterNodePackageResponse](../../models/operations/postmasternodepackageresponse.md)**

