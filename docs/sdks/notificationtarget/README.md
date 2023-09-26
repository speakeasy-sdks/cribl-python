# NotificationTarget

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.NotificationTargetBase(
    id='cf9e06e3-a437-4000-ae6b-6bc9b8f759ea',
    system_fields=[
        'impedit',
    ],
    type=shared.NotificationTargetBaseOutputType.BULLETIN_MESSAGE,
)

res = s.notification_target.create(req)

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateNotificationTargetResponse](../../models/operations/createnotificationtargetresponse.md)**


## delete

Delete NotificationTarget

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.notification_target.delete(id='corporis')

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.notification_target.get(id='est')

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.notification_target.update(id='error', request_body=shared.NotificationTargetBulletinMessage(
    id='41d31135-2965-4bb8-a720-2611435e139d',
    severity=shared.NotificationTargetBulletinMessageSeverity.INFO,
    system_fields=[
        'maxime',
    ],
    text='quia',
    title='Mr.',
    type=shared.NotificationTargetBulletinMessageType.BULLETIN_MESSAGE,
))

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                               | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `id`                                    | *str*                                   | :heavy_check_mark:                      | Unique ID                               |
| `request_body`                          | *Optional[Any]*                         | :heavy_minus_sign:                      | NotificationTarget object to be updated |


### Response

**[operations.UpdatetNotificationTargetResponse](../../models/operations/updatetnotificationtargetresponse.md)**

