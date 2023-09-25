# UserObject

### Available Operations

* [get](#get) - Get a list of User objects
* [update](#update) - Update User except for their roles

## get

Get a list of User objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.user_object.get()

if res.users is not None:
    # handle response
```


### Response

**[operations.GetUserObjectResponse](../../models/operations/getuserobjectresponse.md)**


## update

Update User except for their roles

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.user_object.update(id='culpa', user=shared.User(
    current_password='voluptatum',
    disabled=False,
    email='Princess.Wolff@yahoo.com',
    first='ullam',
    id='a6fae54e-bf60-4c32-9f02-3b75d2367fe1',
    last='est',
    password='accusantium',
    roles=[
        'quod',
    ],
    username='Petra_Lubowitz48',
))

if res.users is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | Unique ID                                            |
| `user`                                               | [Optional[shared.User]](../../models/shared/user.md) | :heavy_minus_sign:                                   | User object                                          |


### Response

**[operations.UpdateUserObjectResponse](../../models/operations/updateuserobjectresponse.md)**

