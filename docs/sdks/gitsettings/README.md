# GitSettings

### Available Operations

* [get](#get) - Get git settings
* [update](#update) - Update git settings

## get

Get git settings

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.git_settings.get()

if res.git_settings_response is not None:
    # handle response
```


### Response

**[operations.GetGitSettingsResponse](../../models/operations/getgitsettingsresponse.md)**


## update

Update git settings

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.git_settings.update()

if res.git_settings is not None:
    # handle response
```


### Response

**[operations.UpdateGitSettingsResponse](../../models/operations/updategitsettingsresponse.md)**

