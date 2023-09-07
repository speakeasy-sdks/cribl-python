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
    group='excepturi',
    id='2601fb57-6b0d-45f0-930c-5fbb25870532',
    metadata=[
        shared.BulletinMessageMetadata(),
    ],
    severity=shared.BulletinMessageSeverity.INFO,
    text='dolores',
    time=793698,
    title='Ms.',
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


res = s.bulletin_message.delete(id='dolor')

if res.bulletin_message is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.bulletin_message.get(id='vero')

if res.bulletin_message is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetBulletinMessageResponse](../../models/operations/getbulletinmessageresponse.md)**

