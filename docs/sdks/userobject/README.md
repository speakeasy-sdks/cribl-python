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

req = operations.UpdateUserObjectRequest(
    user=shared.User(
        current_password='nobis',
        disabled=False,
        email='Caroline_Bashirian@yahoo.com',
        first='deserunt',
        id='b750052a-5647-4edc-839e-d8c4320f4124',
        last='voluptatem',
        password='temporibus',
        roles=[
            'incidunt',
            'totam',
        ],
        username='Jayde.OConner59',
    ),
    id='3b94c3b9-d248-48d7-95aa-42fc405669f6',
)

res = s.user_object.update(req)

if res.users is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateUserObjectRequest](../../models/operations/updateuserobjectrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateUserObjectResponse](../../models/operations/updateuserobjectresponse.md)**

