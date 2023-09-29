# AuthenticationSettings
(*authentication_settings*)

### Available Operations

* [get](#get) - Get authentication settings
* [update](#update) - Update authentication settings

## get

Get authentication settings

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.authentication_settings.get()

if res.auth_configs is not None:
    # handle response
```


### Response

**[operations.GetAuthenticationSettingsResponse](../../models/operations/getauthenticationsettingsresponse.md)**


## update

Update authentication settings

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.authentication_settings.update()

if res.auth_configs is not None:
    # handle response
```


### Response

**[operations.UpdateAuthenticationSettingsResponse](../../models/operations/updateauthenticationsettingsresponse.md)**

