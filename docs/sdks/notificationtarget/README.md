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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.NotificationTargetBulletinMessageSchemas(
    id='<id>',
    type=components.SchemasOutputType.BULLETIN_MESSAGE,
)

res = s.notification_target.create(req)

if res.notification_targets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                                                                                                                                                                  | [Union[components.Schemas, components.NotificationTargetDefaultSchemas, components.NotificationTargetWebhookSchemas, components.NotificationTargetBulletinMessageSchemas, components.NotificationTargetRouterSchemas, components.NotificationTargetNotificationsLogSchemas, components.NotificationTargetPagerDutySchemas]](../../models/components/notificationtarget.md) | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                                                                                                                                                                                 |


### Response

**[operations.CreateNotificationTargetResponse](../../models/operations/createnotificationtargetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete NotificationTarget

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification_target.delete(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get NotificationTarget by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification_target.get(id='<value>')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update NotificationTarget

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.notification_target.update(id='<value>', notification_target=components.NotificationTargetPagerDutySchemas(
    id='<id>',
    routing_key='<value>',
    type=components.SchemasNotificationTargetPagerDutyOutputType.DEFAULT,
))

if res.notification_targets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                   | Unique ID                                                                                                                                                                                                                                                                                                                                                                            |
| `notification_target`                                                                                                                                                                                                                                                                                                                                                                | [Optional[Union[components.Schemas, components.NotificationTargetDefaultSchemas, components.NotificationTargetWebhookSchemas, components.NotificationTargetBulletinMessageSchemas, components.NotificationTargetRouterSchemas, components.NotificationTargetNotificationsLogSchemas, components.NotificationTargetPagerDutySchemas]]](../../models/components/notificationtarget.md) | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                   | NotificationTarget object to be updated                                                                                                                                                                                                                                                                                                                                              |


### Response

**[operations.UpdatetNotificationTargetResponse](../../models/operations/updatetnotificationtargetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
