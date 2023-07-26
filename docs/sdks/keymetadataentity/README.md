# key_metadata_entity

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.KeyMetadataEntity(
    algorithm=shared.KeyMetadataEntityEncryptionAlgorithm.AES_256_CBC,
    cipher_key='numquam',
    created=947822,
    description='adipisci',
    expires=728559,
    key_id='in',
    keyclass=329651,
    kms=shared.KeyMetadataEntityKMSForThisKey.LOCAL,
    plain_key='ex',
    use_iv=False,
)

res = s.key_metadata_entity.create(req)

if res.key_metadata_entities is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.key_metadata_entity.delete('minus')

if res.key_metadata_entities is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.key_metadata_entity.get('ab')

if res.key_metadata_entities is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.key_metadata_entity.update('beatae', shared.KeyMetadataEntity(
    algorithm=shared.KeyMetadataEntityEncryptionAlgorithm.AES_256_GCM,
    cipher_key='nisi',
    created=786954,
    description='dolor',
    expires=496548,
    key_id='fuga',
    keyclass=326903,
    kms=shared.KeyMetadataEntityKMSForThisKey.LOCAL,
    plain_key='architecto',
    use_iv=False,
))

if res.key_metadata_entities is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | Unique ID                                                                      |
| `key_metadata_entity`                                                          | [Optional[shared.KeyMetadataEntity]](../../models/shared/keymetadataentity.md) | :heavy_minus_sign:                                                             | KeyMetadataEntity object to be updated                                         |


### Response

**[operations.UpdateKeyMetadataEntityResponse](../../models/operations/updatekeymetadataentityresponse.md)**

