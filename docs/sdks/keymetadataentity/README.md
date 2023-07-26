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
    cipher_key='explicabo',
    created=380450,
    description='ipsa',
    expires=910410,
    key_id='sint',
    keyclass=749537,
    kms=shared.KeyMetadataEntityKMSForThisKey.LOCAL,
    plain_key='qui',
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

req = operations.DeleteKeyMetadataEntityRequest(
    id='00ce78a1-bd8f-4b7a-8a11-6ce723d4097f',
)

res = s.key_metadata_entity.delete(req)

if res.key_metadata_entities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteKeyMetadataEntityRequest](../../models/operations/deletekeymetadataentityrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


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

req = operations.GetKeyMetadataEntityRequest(
    id='a30e9af7-25b2-4912-a030-d83f5aeb7799',
)

res = s.key_metadata_entity.get(req)

if res.key_metadata_entities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetKeyMetadataEntityRequest](../../models/operations/getkeymetadataentityrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


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

req = operations.UpdateKeyMetadataEntityRequest(
    key_metadata_entity=shared.KeyMetadataEntity(
        algorithm=shared.KeyMetadataEntityEncryptionAlgorithm.AES_256_GCM,
        cipher_key='sunt',
        created=142856,
        description='vero',
        expires=533723,
        key_id='optio',
        keyclass=98805,
        kms=shared.KeyMetadataEntityKMSForThisKey.LOCAL,
        plain_key='repellat',
        use_iv=False,
    ),
    id='8493825f-dc42-4c87-ac2c-2dfb4cfc1c76',
)

res = s.key_metadata_entity.update(req)

if res.key_metadata_entities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateKeyMetadataEntityRequest](../../models/operations/updatekeymetadataentityrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateKeyMetadataEntityResponse](../../models/operations/updatekeymetadataentityresponse.md)**

