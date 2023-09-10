# user_object

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


res = s.user_object.update(id='sunt', user=shared.User(
    current_password='enim',
    disabled=False,
    email='Wilfredo_Rau@hotmail.com',
    first='accusamus',
    id='188b1c4e-e2c8-4c6c-a611-feeb1c7cbdb6',
    last='saepe',
    password='earum',
    roles=[
        'quod',
    ],
    username='Janet49',
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

