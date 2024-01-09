# UserProperties
(*user_properties*)

### Available Operations

* [update](#update) - Update User properties – admin use only

## update

Update User properties – admin use only

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user_properties.update(id='string', user_profile=components.UserProfile(
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

if res.user_profiles is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | Unique ID                                                                  |
| `user_profile`                                                             | [Optional[components.UserProfile]](../../models/components/userprofile.md) | :heavy_minus_sign:                                                         | UserProfile object                                                         |


### Response

**[operations.UpdateUserPropertiesResponse](../../models/operations/updateuserpropertiesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
