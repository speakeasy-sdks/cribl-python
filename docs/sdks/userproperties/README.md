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


res = s.user_properties.update(id='laudantium', user_profile=shared.UserProfile(
    disabled=False,
    email='Luis19@hotmail.com',
    first='beatae',
    id='7747dc91-5ad2-4caf-9dd6-723dc0f5ae2f',
    last='neque',
    password='officia',
    roles=[
        'suscipit',
    ],
    username='Martine2',
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

