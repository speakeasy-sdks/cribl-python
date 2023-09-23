# User

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
    current_password='consequatur',
    disabled=False,
    email='Silas_Schumm30@yahoo.com',
    first='dolorum',
    id='a5f3cabd-905a-4972-a056-728227b2d309',
    last='dolore',
    password='esse',
    roles=[
        'accusantium',
    ],
    username='Milan_Will',
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

