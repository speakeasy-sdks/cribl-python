# CriblsSettings
(*cribls_settings*)

### Available Operations

* [~~get~~](#get) - Get Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/redis-cache-limits, /system/services-limits, /system/settings/git-settings, and /system/settings/conf respectively :warning: **Deprecated**
* [~~update~~](#update) - Update Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/settings/git-settings, /system/settings/auth and /system/settings/conf respectively :warning: **Deprecated**

## ~~get~~

Get Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/redis-cache-limits, /system/services-limits, /system/settings/git-settings, and /system/settings/conf respectively

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.cribls_settings.get()

if res.git_settings is not None:
    # handle response
    pass
```


### Response

**[operations.GetCriblsSettingsResponse](../../models/operations/getcriblssettingsresponse.md)**


## ~~update~~

Update Cribl system settings. Deprecated: use specific endpoints /system/limits, /system/job-limits, /system/settings/git-settings, /system/settings/auth and /system/settings/conf respectively

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.cribls_settings.update()

if res.git_settings is not None:
    # handle response
    pass
```


### Response

**[operations.UpdateCriblsSettingsResponse](../../models/operations/updatecriblssettingsresponse.md)**

