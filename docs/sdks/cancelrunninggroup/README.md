# cancel_running_group

### Available Operations

* [post](#post) - Cancel a running group upgrade

## post

Cancel a running group upgrade

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.cancel_running_group.post(group='adipisci')

if res.cancel_running_group is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group`            | *str*              | :heavy_check_mark: | id of the group    |


### Response

**[operations.PostCancelRunningGroupResponse](../../models/operations/postcancelrunninggroupresponse.md)**

