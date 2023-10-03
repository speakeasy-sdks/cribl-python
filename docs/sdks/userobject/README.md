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


res = s.user_object.update(id='Van', user=shared.User(
    current_password='Reactive',
    disabled=False,
    email='Don.Murazik44@hotmail.com',
    first='Arizona Cotton extend',
    id='<ID>',
    last='bifurcated',
    password='kuAMJjbGSAhBnJP',
    roles=[
        'Wooden',
    ],
    username='Fermin_Herman',
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

