# RestSecret

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
    api_key='incidunt',
    description='qui',
    id='2eb2164c-f9ab-4836-ac72-3ffda9e06bee',
    password='non',
    secret_key='rem',
    secret_type=shared.SecretType.TEXT,
    tags='ullam',
    username='Pansy_Carter6',
    value='officiis',
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


res = s.rest_secret.delete(id='architecto')

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


res = s.rest_secret.get(id='architecto')

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


res = s.rest_secret.update(id='enim', rest_secret=shared.RestSecret(
    api_key='optio',
    description='rem',
    id='0bff9185-44ec-442d-afcc-e8f1977773e6',
    password='neque',
    secret_key='corporis',
    secret_type=shared.SecretType.KEYPAIR,
    tags='consequuntur',
    username='Lucio.Kiehn5',
    value='rem',
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

