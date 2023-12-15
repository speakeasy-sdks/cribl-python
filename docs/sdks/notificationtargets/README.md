# NotificationTargets
(*notification_targets*)

### Available Operations

* [get](#get) - Get a list of NotificationTarget objects

## get

Get a list of NotificationTarget objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification_targets.get()

if res.notification_targets is not None:
    # handle response
    pass
```


### Response

**[operations.GetNotificationTargetsResponse](../../models/operations/getnotificationtargetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
