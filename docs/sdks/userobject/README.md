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


res = s.user_object.update(id='mollitia', user=shared.User(
    current_password='accusamus',
    disabled=False,
    email='Odie_Baumbach5@hotmail.com',
    first='deserunt',
    id='6924d3b2-ecfc-4c8f-8950-10f5dd3d6fa1',
    last='quos',
    password='aperiam',
    roles=[
        'non',
    ],
    username='Tate78',
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

