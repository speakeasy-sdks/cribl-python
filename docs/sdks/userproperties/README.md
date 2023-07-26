# user_properties

### Available Operations

* [update](#update) - Update User properties – admin use only

## update

Update User properties – admin use only

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateUserPropertiesRequest(
    user_profile=shared.UserProfile(
        disabled=False,
        email='Madilyn37@yahoo.com',
        first='pariatur',
        id='21249450-819d-47c3-b1b4-1844060e0031',
        last='ipsa',
        password='possimus',
        roles=[
            'qui',
        ],
        username='Deja_Sipes5',
    ),
    id='1f5afd2a-6c44-4846-ae9d-89253c8962f4',
)

res = s.user_properties.update(req)

if res.user_profiles is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateUserPropertiesRequest](../../models/operations/updateuserpropertiesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateUserPropertiesResponse](../../models/operations/updateuserpropertiesresponse.md)**

