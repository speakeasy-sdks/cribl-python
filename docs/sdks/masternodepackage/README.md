# MasterNodePackage
(*.master_node_package*)

### Available Operations

* [post](#post) - Upgrade master node with the provided package

## post

Upgrade master node with the provided package

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.UpgradeMasterRequest(
    packages=[
        components.Packages(
            package_url='string',
        ),
    ],
)

res = s.master_node_package.post(req)

if res.cribl is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.UpgradeMasterRequest](../../models/shared/upgrademasterrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PostMasterNodePackageResponse](../../models/operations/postmasternodepackageresponse.md)**

