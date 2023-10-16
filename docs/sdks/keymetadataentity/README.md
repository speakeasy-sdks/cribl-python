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
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.KeyMetadataEntity(
    key_id='bluetooth Extended',
)

res = s.key_metadata_entity.create(req)

if res.key_metadata_entities is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.KeyMetadataEntity](../../models/shared/keymetadataentity.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateKeyMetadataEntityResponse](../../models/operations/createkeymetadataentityresponse.md)**


## delete

Delete KeyMetadataEntity

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.key_metadata_entity.delete(id='program')

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


## get

Get KeyMetadataEntity by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.key_metadata_entity.get(id='female')

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


## update

Update KeyMetadataEntity

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.key_metadata_entity.update(id='Van', key_metadata_entity=shared.KeyMetadataEntity(
    key_id='Reactive',
))

if res.key_metadata_entities is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | Unique ID                                                                      |
| `key_metadata_entity`                                                          | [Optional[shared.KeyMetadataEntity]](../../models/shared/keymetadataentity.md) | :heavy_minus_sign:                                                             | KeyMetadataEntity object to be updated                                         |


### Response

**[operations.UpdateKeyMetadataEntityResponse](../../models/operations/updatekeymetadataentityresponse.md)**

