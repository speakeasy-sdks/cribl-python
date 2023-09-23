# NotificationTargets

### Available Operations

* [get](#get) - Get a list of NotificationTarget objects

## get

Get a list of NotificationTarget objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.notification_targets.get()

if res.notification_targets is not None:
    # handle response
```


### Response

**[operations.GetNotificationTargetsResponse](../../models/operations/getnotificationtargetsresponse.md)**

