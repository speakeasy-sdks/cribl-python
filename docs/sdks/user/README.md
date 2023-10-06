# User
(*user*)

### Available Operations

* [create_user](#create_user) - Create User

## create_user

Create User

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.User(
    current_password='Jeep Ford',
    disabled=False,
    email='Sean.Brown40@hotmail.com',
    first='crossly',
    id='<ID>',
    last='iterate South Delaware',
    password='JJFZd3JtxWkW1UM',
    roles=[
        'intuitive',
    ],
    username='Lucinda56',
)

res = s.user.create_user(req)

if res.users is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**

