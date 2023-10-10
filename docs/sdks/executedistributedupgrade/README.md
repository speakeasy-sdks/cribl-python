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


res = s.execute_distributed_upgrade.post(group='payment', request_body={
    "Silver": 'iste',
})

if res.cribl_package is not None:
    # handle response
```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `group`                   | *str*                     | :heavy_check_mark:        | Group to upgrade          |
| `request_body`            | dict[str, *Any*]          | :heavy_minus_sign:        | distributedUpgrade object |


### Response

**[operations.PostExecuteDistributedUpgradeResponse](../../models/operations/postexecutedistributedupgraderesponse.md)**

