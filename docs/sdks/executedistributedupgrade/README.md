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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.execute_distributed_upgrade.post(group='reiciendis', distributed_upgrade_request=shared.DistributedUpgradeRequest(
    package_urls=[
        shared.DistributedUpgradeRequestPackageUrls(
            package_hash_url='quidem',
            package_url='saepe',
        ),
    ],
    upgrade_mode=shared.DistributedUpgradeRequestUpgradeMode.REGULAR,
    upgrade_percentage=296556,
    worker_retries=121059,
    worker_retry_delay=992012,
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

