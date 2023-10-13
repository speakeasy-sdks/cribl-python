# UserObject
(*user_object*)

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
    bearer_auth="",
)


res = s.user_object.get()

if res.users is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.user_object.update(id='Van', user=shared.User(
    disabled=False,
    email='Evie.Quitzon62@gmail.com',
    first='redundant cheater Islands',
    id='<ID>',
    last='withdrawal extend',
    roles=[
        'Plastic',
    ],
    username='Brody_Nolan88',
))

if res.users is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | Unique ID                                            |
| `user`                                               | [Optional[shared.User]](../../models/shared/user.md) | :heavy_minus_sign:                                   | User object                                          |


### Response

**[operations.UpdateUserObjectResponse](../../models/operations/updateuserobjectresponse.md)**

