# CriblSystemSettings

### Available Operations

* [get](#get) - Get Cribl system settings
* [update](#update) - Update Cribl system settings

## get

Get Cribl system settings

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.cribl_system_settings.get()

if res.system_settings is not None:
    # handle response
```


### Response

**[operations.GetCriblSystemSettingsResponse](../../models/operations/getcriblsystemsettingsresponse.md)**


## update

Update Cribl system settings

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.cribl_system_settings.update()

if res.system_settingses is not None:
    # handle response
```


### Response

**[operations.UpdateCriblSystemSettingsResponse](../../models/operations/updatecriblsystemsettingsresponse.md)**

