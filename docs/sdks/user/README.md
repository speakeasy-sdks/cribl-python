# user

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
    current_password='voluptas',
    disabled=False,
    email='Jeff69@gmail.com',
    first='aperiam',
    id='d51a44bf-01ba-4d87-86d4-6082bfbdc41f',
    last='delectus',
    password='nemo',
    roles=[
        'magnam',
        'officiis',
        'sed',
        'mollitia',
    ],
    username='Stephen_Green32',
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

