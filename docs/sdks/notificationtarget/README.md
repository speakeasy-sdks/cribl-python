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

req = shared.NotificationTargetNotificationsLog(
    id='2259b1ab-da8c-4070-a108-4cb0672d1ad8',
    logs_dir='molestiae',
    system_fields=[
        'provident',
    ],
    type=shared.NotificationTargetNotificationsLogType.NOTIFICATIONS_LOG,
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


res = s.notification_target.delete(id='accusamus')

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


res = s.notification_target.get(id='necessitatibus')

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


res = s.notification_target.update(id='tempore', request_body=shared.NotificationTargetRouter(
    id='665b85ef-bd02-4bae-8be2-d782259e3ea4',
    rules=[
        shared.NotificationTargetRouterRules(
            description='quidem',
            filter='quis',
            final=False,
            output='beatae',
        ),
    ],
    system_fields=[
        'unde',
    ],
    type=shared.NotificationTargetRouterType.ROUTER,
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

