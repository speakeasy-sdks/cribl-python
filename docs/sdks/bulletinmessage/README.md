# BulletinMessage
(*bulletin_message*)

### Available Operations

* [create](#create) - Create BulletinMessage
* [delete](#delete) - Delete BulletinMessage
* [get](#get) - Get BulletinMessage by ID

## create

Create BulletinMessage

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.BulletinMessage(
    id='<id>',
    text='<value>',
)

res = s.bulletin_message.create(req)

if res.bulletin_message is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.BulletinMessage](../../models/components/bulletinmessage.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateBulletinMessageResponse](../../models/operations/createbulletinmessageresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete BulletinMessage

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.bulletin_message.delete(id='<value>')

if res.bulletin_message is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteBulletinMessageResponse](../../models/operations/deletebulletinmessageresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get BulletinMessage by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.bulletin_message.get(id='<value>')

if res.bulletin_message is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetBulletinMessageResponse](../../models/operations/getbulletinmessageresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
