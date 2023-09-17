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
    api_key='reiciendis',
    description='ab',
    id='977773e6-3562-4a7b-808f-05e3d48fdaf3',
    password='vitae',
    secret_key='nesciunt',
    secret_type=shared.SecretType.KEYPAIR,
    tags='illo',
    username='Zoe_Hettinger60',
    value='incidunt',
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


res = s.rest_secret.delete(id='explicabo')

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


res = s.rest_secret.get(id='ipsam')

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


res = s.rest_secret.update(id='cupiditate', rest_secret=shared.RestSecret(
    api_key='optio',
    description='alias',
    id='b36f25ea-944f-43b7-96c1-1f6c37a51262',
    password='incidunt',
    secret_key='adipisci',
    secret_type=shared.SecretType.KEYPAIR,
    tags='dolor',
    username='Faye_Quitzon2',
    value='nemo',
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

