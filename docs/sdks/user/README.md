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
    current_password='molestias',
    disabled=False,
    email='Brandi13@gmail.com',
    first='earum',
    id='55055756-f5d5-46d0-bd0a-f2dfe13db4f6',
    last='explicabo',
    password='minus',
    roles=[
        'soluta',
    ],
    username='Marianne_Flatley62',
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

