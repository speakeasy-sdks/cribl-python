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
    current_password='quo',
    disabled=False,
    email='Julius77@hotmail.com',
    first='facere',
    id='4258d035-8a82-4c80-8fe2-751a2047c044',
    last='omnis',
    password='repudiandae',
    roles=[
        'quaerat',
    ],
    username='Colt.Weissnat',
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

