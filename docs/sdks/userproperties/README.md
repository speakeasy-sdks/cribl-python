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
    bearer_auth="",
)


res = s.user_properties.update(id='Van', user_profile=shared.UserProfile(
    disabled=False,
    email='Evie.Quitzon62@gmail.com',
    first='Analyst',
    id='<ID>',
    last='invoice',
    roles=[
        'Arizona',
    ],
    username='Dudley.Treutel',
))

if res.user_profiles is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Unique ID                                                          |
| `user_profile`                                                     | [Optional[shared.UserProfile]](../../models/shared/userprofile.md) | :heavy_minus_sign:                                                 | UserProfile object                                                 |


### Response

**[operations.UpdateUserPropertiesResponse](../../models/operations/updateuserpropertiesresponse.md)**

