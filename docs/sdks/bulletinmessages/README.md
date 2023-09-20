# BulletinMessages

### Available Operations

* [get](#get) - Get a list of BulletinMessage objects

## get

Get a list of BulletinMessage objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.bulletin_messages.get()

if res.bulletin_messages is not None:
    # handle response
```


### Response

**[operations.GetBulletinMessagesResponse](../../models/operations/getbulletinmessagesresponse.md)**

