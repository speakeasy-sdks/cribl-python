# KeyMetadataEntity
(*key_metadata_entity*)

### Available Operations

* [create](#create) - Create KeyMetadataEntity
* [delete](#delete) - Delete KeyMetadataEntity
* [get](#get) - Get KeyMetadataEntity by ID
* [update](#update) - Update KeyMetadataEntity

## create

Create KeyMetadataEntity

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.KeyMetadataEntity(
    key_id='<value>',
)

res = s.key_metadata_entity.create(req)

if res.key_metadata_entities is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.KeyMetadataEntity](../../models/components/keymetadataentity.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateKeyMetadataEntityResponse](../../models/operations/createkeymetadataentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete KeyMetadataEntity

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.key_metadata_entity.delete(id='<value>')

if res.key_metadata_entities is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteKeyMetadataEntityResponse](../../models/operations/deletekeymetadataentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get KeyMetadataEntity by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.key_metadata_entity.get(id='<value>')

if res.key_metadata_entities is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetKeyMetadataEntityResponse](../../models/operations/getkeymetadataentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update KeyMetadataEntity

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.key_metadata_entity.update(id='<value>', key_metadata_entity=components.KeyMetadataEntity(
    key_id='<value>',
))

if res.key_metadata_entities is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique ID                                                                              |
| `key_metadata_entity`                                                                  | [Optional[components.KeyMetadataEntity]](../../models/components/keymetadataentity.md) | :heavy_minus_sign:                                                                     | KeyMetadataEntity object to be updated                                                 |


### Response

**[operations.UpdateKeyMetadataEntityResponse](../../models/operations/updatekeymetadataentityresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
