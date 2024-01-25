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

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_object.get()

if res.users is not None:
    # handle response
    pass
```


### Response

**[operations.GetUserObjectResponse](../../models/operations/getuserobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update User except for their roles

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_object.update(id='string', user=components.User(
    disabled=False,
    email='Alberto34@hotmail.com',
    first='string',
    id='<ID>',
    last='string',
    roles=[
        'string',
    ],
    username='Mellie62',
))

if res.users is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique ID                                                    |
| `user`                                                       | [Optional[components.User]](../../models/components/user.md) | :heavy_minus_sign:                                           | User object                                                  |


### Response

**[operations.UpdateUserObjectResponse](../../models/operations/updateuserobjectresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
