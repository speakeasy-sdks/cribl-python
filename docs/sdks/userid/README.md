# user_id

### Available Operations

* [delete](#delete) - Delete User
* [get](#get) - Get User by ID

## delete

Delete User

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteUserIDRequest(
    id='19bb7d40-d5a1-41fa-836e-6259233f95c9',
)

res = s.user_id.delete(req)

if res.users is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteUserIDRequest](../../models/operations/deleteuseridrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteUserIDResponse](../../models/operations/deleteuseridresponse.md)**


## get

Get User by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetUserIDRequest(
    id='d237397c-785b-45db-8f50-0183febdf676',
)

res = s.user_id.get(req)

if res.users is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetUserIDRequest](../../models/operations/getuseridrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetUserIDResponse](../../models/operations/getuseridresponse.md)**

