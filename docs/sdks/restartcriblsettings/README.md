# RestartCriblSettings
(*restart_cribl_settings*)

### Available Operations

* [post](#post) - Restart Cribl server

## post

Restart Cribl server

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.restart_cribl_settings.post()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostRestartCriblSettingsResponse](../../models/operations/postrestartcriblsettingsresponse.md)**

