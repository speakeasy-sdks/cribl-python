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

req = operations.PostExecuteDistributedUpgradeRequest(
    distributed_upgrade_request=shared.DistributedUpgradeRequest(
        package_urls=[
            shared.DistributedUpgradeRequestPackageUrls(
                package_hash_url='nesciunt',
                package_url='delectus',
            ),
        ],
        upgrade_mode=shared.DistributedUpgradeRequestUpgradeMode.REGULAR,
        upgrade_percentage=303421,
        worker_retries=644223,
        worker_retry_delay=266680,
    ),
    group='sunt',
)

res = s.execute_distributed_upgrade.post(req)

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostExecuteDistributedUpgradeRequest](../../models/operations/postexecutedistributedupgraderequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PostExecuteDistributedUpgradeResponse](../../models/operations/postexecutedistributedupgraderesponse.md)**

