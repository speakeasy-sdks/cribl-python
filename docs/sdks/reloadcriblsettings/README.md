# reload_cribl_settings

### Available Operations

* [post](#post) - Reload Cribl settings from the filesystem

## post

Reload Cribl settings from the filesystem

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.reload_cribl_settings.post()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostReloadCriblSettingsResponse](../../models/operations/postreloadcriblsettingsresponse.md)**

