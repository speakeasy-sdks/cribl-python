# ExecuteDistributedUpgrade
(*execute_distributed_upgrade*)

### Available Operations

* [post](#post) - Execute distributed group upgrade

## post

Execute distributed group upgrade

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.execute_distributed_upgrade.post(group='payment', distributed_upgrade_request=shared.DistributedUpgradeRequest(
    package_urls=[
        shared.DistributedUpgradeRequestPackageUrls(
            package_url='base mealy Metrics',
        ),
    ],
))

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `group`                                                                                        | *str*                                                                                          | :heavy_check_mark:                                                                             | Group to upgrade                                                                               |
| `distributed_upgrade_request`                                                                  | [Optional[shared.DistributedUpgradeRequest]](../../models/shared/distributedupgraderequest.md) | :heavy_minus_sign:                                                                             | distributedUpgrade object                                                                      |


### Response

**[operations.PostExecuteDistributedUpgradeResponse](../../models/operations/postexecutedistributedupgraderesponse.md)**

