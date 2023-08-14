# rest_secret

### Available Operations

* [create](#create) - Create RestSecret
* [delete](#delete) - Delete RestSecret
* [get](#get) - Get RestSecret by ID
* [update](#update) - Update RestSecret

## create

Create RestSecret

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.RestSecret(
    api_key='suscipit',
    description='quibusdam',
    id='dca8ef51-fcb4-4c59-bec1-2cdaad0ec7af',
    password='saepe',
    secret_key='facere',
    secret_type=shared.SecretType.CREDENTIALS,
    tags='at',
    username='Kelli_Ankunding27',
    value='numquam',
)

res = s.rest_secret.create(req)

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.RestSecret](../../models/shared/restsecret.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateRestSecretResponse](../../models/operations/createrestsecretresponse.md)**


## delete

Delete RestSecret

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.rest_secret.delete(id='corrupti')

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteRestSecretResponse](../../models/operations/deleterestsecretresponse.md)**


## get

Get RestSecret by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.rest_secret.get(id='similique')

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetRestSecretResponse](../../models/operations/getrestsecretresponse.md)**


## update

Update RestSecret

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.rest_secret.update(id='dolore', rest_secret=shared.RestSecret(
    api_key='esse',
    description='reiciendis',
    id='9390c588-8098-43da-bf9e-f3ffdd9f7f07',
    password='omnis',
    secret_key='similique',
    secret_type=shared.SecretType.CREDENTIALS,
    tags='modi',
    username='Rebecca.Durgan',
    value='sed',
))

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Unique ID                                                        |
| `rest_secret`                                                    | [Optional[shared.RestSecret]](../../models/shared/restsecret.md) | :heavy_minus_sign:                                               | RestSecret object to be updated                                  |


### Response

**[operations.UpdateRestSecretResponse](../../models/operations/updaterestsecretresponse.md)**

