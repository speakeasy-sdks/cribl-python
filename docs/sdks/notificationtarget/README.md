# NotificationTarget
(*notification_target*)

### Available Operations

* [create](#create) - Create NotificationTarget
* [delete](#delete) - Delete NotificationTarget
* [get](#get) - Get NotificationTarget by ID
* [update](#update) - Update NotificationTarget

## create

Create NotificationTarget

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.NotificationTargetNotificationTargetBulletinMessage(
    id='<ID>',
    system_fields=[
        'bluetooth',
    ],
    type=shared.NotificationTargetNotificationTargetBulletinMessageType.BULLETIN_MESSAGE,
)

res = s.notification_target.create(req)

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Union[shared.NotificationTargetNotificationTargetBase, shared.NotificationTargetNotificationTargetDefault, shared.NotificationTargetNotificationTargetWebhook, shared.NotificationTargetNotificationTargetBulletinMessage, shared.NotificationTargetNotificationTargetRouter, shared.NotificationTargetNotificationTargetNotificationsLog, shared.NotificationTargetNotificationTargetPagerDuty]](../../models/shared/notificationtarget.md) | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                            | The request object to use for the request.                                                                                                                                                                                                                                                                                                                                                                                                    |


### Response

**[operations.CreateNotificationTargetResponse](../../models/operations/createnotificationtargetresponse.md)**


## delete

Delete NotificationTarget

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.notification_target.delete(id='program')

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeletetNotificationTargetResponse](../../models/operations/deletetnotificationtargetresponse.md)**


## get

Get NotificationTarget by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.notification_target.get(id='female')

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetNotificationTargetResponse](../../models/operations/getnotificationtargetresponse.md)**


## update

Update NotificationTarget

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.notification_target.update(id='Van', notification_target=shared.NotificationTargetNotificationTargetBase(
    id='<ID>',
    system_fields=[
        'Reactive',
    ],
    type=shared.NotificationTargetNotificationTargetBaseOutputType.PAGER_DUTY,
))

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                      | Unique ID                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `notification_target`                                                                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[Union[shared.NotificationTargetNotificationTargetBase, shared.NotificationTargetNotificationTargetDefault, shared.NotificationTargetNotificationTargetWebhook, shared.NotificationTargetNotificationTargetBulletinMessage, shared.NotificationTargetNotificationTargetRouter, shared.NotificationTargetNotificationTargetNotificationsLog, shared.NotificationTargetNotificationTargetPagerDuty]]](../../models/shared/notificationtarget.md) | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                      | NotificationTarget object to be updated                                                                                                                                                                                                                                                                                                                                                                                                                 |


### Response

**[operations.UpdatetNotificationTargetResponse](../../models/operations/updatetnotificationtargetresponse.md)**

