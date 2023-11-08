# User
(*.user*)

### Available Operations

* [create_user](#create_user) - Create User

## create_user

Create User

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.User(
    disabled=False,
    email='Richie.Kuhic95@yahoo.com',
    first='string',
    id='<ID>',
    last='string',
    roles=[
        'string',
    ],
    username='Sean.Brown40',
)

res = s.user.create_user(req)

if res.users is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                      | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `request`                                      | [components.User](../../models/shared/user.md) | :heavy_check_mark:                             | The request object to use for the request.     |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
