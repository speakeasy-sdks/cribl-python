# UserProperties

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


res = s.user_properties.update(id='provident', user_profile=shared.UserProfile(
    disabled=False,
    email='Alverta59@hotmail.com',
    first='ex',
    id='d90c364b-7c15-4dfb-ace1-88b1c4ee2c8c',
    last='vel',
    password='eligendi',
    roles=[
        'recusandae',
    ],
    username='Gunnar98',
))

if res.user_profiles is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Unique ID                                                          |
| `user_profile`                                                     | [Optional[shared.UserProfile]](../../models/shared/userprofile.md) | :heavy_minus_sign:                                                 | UserProfile object                                                 |


### Response

**[operations.UpdateUserPropertiesResponse](../../models/operations/updateuserpropertiesresponse.md)**

