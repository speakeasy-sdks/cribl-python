# bulletin_message

### Available Operations

* [create](#create) - Create BulletinMessage
* [delete](#delete) - Delete BulletinMessage
* [get](#get) - Get BulletinMessage by ID

## create

Create BulletinMessage

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.BulletinMessage(
    group='provident',
    id='dfe0ab7d-a8a5-40ce-987f-86bc173d689e',
    metadata=[
        shared.BulletinMessageMetadata(),
        shared.BulletinMessageMetadata(),
        shared.BulletinMessageMetadata(),
        shared.BulletinMessageMetadata(),
    ],
    severity=shared.BulletinMessageSeverity.FATAL,
    text='natus',
    time=328303,
    title='Mr.',
)

res = s.bulletin_message.create(req)

if res.bulletin_message is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.BulletinMessage](../../models/shared/bulletinmessage.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateBulletinMessageResponse](../../models/operations/createbulletinmessageresponse.md)**


## delete

Delete BulletinMessage

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteBulletinMessageRequest(
    id='6f8d986e-881e-4ad4-b0e1-012563f94e29',
)

res = s.bulletin_message.delete(req)

if res.bulletin_message is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteBulletinMessageRequest](../../models/operations/deletebulletinmessagerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteBulletinMessageResponse](../../models/operations/deletebulletinmessageresponse.md)**


## get

Get BulletinMessage by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetBulletinMessageRequest(
    id='e973e922-a57a-415b-a3e0-60807e2b6e3a',
)

res = s.bulletin_message.get(req)

if res.bulletin_message is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetBulletinMessageRequest](../../models/operations/getbulletinmessagerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetBulletinMessageResponse](../../models/operations/getbulletinmessageresponse.md)**

