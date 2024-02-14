# ExecuteDistributedUpgrade
(*execute_distributed_upgrade*)

### Available Operations

* [post](#post) - Execute distributed group upgrade

## post

Execute distributed group upgrade

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.execute_distributed_upgrade.post(group='string', distributed_upgrade_request=components.DistributedUpgradeRequest())

if res.cribl_package is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `group`                                                                                                | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Group to upgrade                                                                                       |
| `distributed_upgrade_request`                                                                          | [Optional[components.DistributedUpgradeRequest]](../../models/components/distributedupgraderequest.md) | :heavy_minus_sign:                                                                                     | distributedUpgrade object                                                                              |


### Response

**[operations.PostExecuteDistributedUpgradeResponse](../../models/operations/postexecutedistributedupgraderesponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
