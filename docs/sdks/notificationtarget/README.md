# notification_target

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

req = shared.NotificationTargetRouter(
    id='26ddb589-461e-4742-9cbe-6d9502f0ea93',
    rules=[
        shared.NotificationTargetRouterRules(
            description='distinctio',
            filter='voluptas',
            final=False,
            output='sint',
        ),
    ],
    system_fields=[
        'nihil',
        'fuga',
        'cumque',
        'consequuntur',
    ],
    type=shared.NotificationTargetRouterType.ROUTER,
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

req = operations.DeletetNotificationTargetRequest(
    id='f72f8850-0904-4911-a082-07888ec66183',
)

res = s.notification_target.delete(req)

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeletetNotificationTargetRequest](../../models/operations/deletetnotificationtargetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


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

req = operations.GetNotificationTargetRequest(
    id='bfe9659e-b40e-4c16-baf7-5b0b532a4da3',
)

res = s.notification_target.get(req)

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetNotificationTargetRequest](../../models/operations/getnotificationtargetrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


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

req = operations.UpdatetNotificationTargetRequest(
    request_body=shared.NotificationTargetBulletinMessage(
        id='cbaaf445-2c48-442c-9b2a-d32dafe81a88',
        severity=shared.NotificationTargetBulletinMessageSeverity.FATAL,
        system_fields=[
            'incidunt',
            'labore',
        ],
        text='ut',
        title='Mrs.',
        type=shared.NotificationTargetBulletinMessageType.BULLETIN_MESSAGE,
    ),
    id='73fecd47-353f-463c-8209-379aa69cd5fb',
)

res = s.notification_target.update(req)

if res.notification_targets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdatetNotificationTargetRequest](../../models/operations/updatetnotificationtargetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.UpdatetNotificationTargetResponse](../../models/operations/updatetnotificationtargetresponse.md)**

