# UserID
(*.user_id*)

### Available Operations

* [delete](#delete) - Delete User
* [get](#get) - Get User by ID

## delete

Delete User

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.user_id.delete(id='string')

if res.users is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteUserIDResponse](../../models/operations/deleteuseridresponse.md)**


## get

Get User by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.user_id.get(id='string')

if res.users is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetUserIDResponse](../../models/operations/getuseridresponse.md)**

