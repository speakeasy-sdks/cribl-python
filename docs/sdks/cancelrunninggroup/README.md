# CancelRunningGroup
(*cancel_running_group*)

### Available Operations

* [post](#post) - Cancel a running group upgrade

## post

Cancel a running group upgrade

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.cancel_running_group.post(group='string')

if res.cancel_running_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group`            | *str*              | :heavy_check_mark: | id of the group    |


### Response

**[operations.PostCancelRunningGroupResponse](../../models/operations/postcancelrunninggroupresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
