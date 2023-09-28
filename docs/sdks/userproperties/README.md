# UserProperties
(*user_properties*)

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


res = s.user_properties.update(id='quas', user_profile=shared.UserProfile(
    disabled=False,
    email='Willow_Bode@gmail.com',
    first='est',
    id='363c8873-e484-4380-b1f6-b8ca275a60a0',
    last='dolore',
    password='maxime',
    roles=[
        'aliquam',
    ],
    username='Lessie_Hermiston37',
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

