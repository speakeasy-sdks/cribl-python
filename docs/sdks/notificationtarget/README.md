# NotificationTarget
(*.notification_target*)

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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.NotificationTargetBulletinMessageSchemas(
    id='<ID>',
    system_fields=[
        'string',
    ],
    type=components.Type.BULLETIN_MESSAGE,
)

res = s.notification_target.create(req)

if res.notification_targets is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.notification_target.delete(id='string')

if res.notification_targets is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.notification_target.get(id='string')

if res.notification_targets is not None:
    # handle response
    pass
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
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.notification_target.update(id='string', request_body=components.NotificationTargetPagerDutySchemas(
    id='<ID>',
    routing_key='string',
    system_fields=[
        'string',
    ],
    type=components.SchemasNotificationTargetPagerDutyType.PAGER_DUTY,
))

if res.notification_targets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                               | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `id`                                    | *str*                                   | :heavy_check_mark:                      | Unique ID                               |
| `request_body`                          | *Optional[Any]*                         | :heavy_minus_sign:                      | NotificationTarget object to be updated |


### Response

**[operations.UpdatetNotificationTargetResponse](../../models/operations/updatetnotificationtargetresponse.md)**

