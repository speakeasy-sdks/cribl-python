# execute_distributed_upgrade

### Available Operations

* [post](#post) - Execute distributed group upgrade

## post

Execute distributed group upgrade

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.execute_distributed_upgrade.post(group='fugiat', distributed_upgrade_request=shared.DistributedUpgradeRequest(
    package_urls=[
        shared.DistributedUpgradeRequestPackageUrls(
            package_hash_url='officiis',
            package_url='ducimus',
        ),
        shared.DistributedUpgradeRequestPackageUrls(
            package_hash_url='dolor',
            package_url='dicta',
        ),
        shared.DistributedUpgradeRequestPackageUrls(
            package_hash_url='error',
            package_url='porro',
        ),
    ],
    upgrade_mode=shared.DistributedUpgradeRequestUpgradeMode.ROLLING,
    upgrade_percentage=491591,
    worker_retries=458970,
    worker_retry_delay=854115,
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

