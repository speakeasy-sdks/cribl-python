# RestSecret
(*.rest_secret*)

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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.RestSecret(
    id='<ID>',
    secret_type=components.SecretType.KEYPAIR,
)

res = s.rest_secret.create(req)

if res.rest_secret is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [components.RestSecret](../../models/shared/restsecret.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateRestSecretResponse](../../models/operations/createrestsecretresponse.md)**


## delete

Delete RestSecret

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.rest_secret.delete(id='string')

if res.rest_secret is not None:
    # handle response
    pass
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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.rest_secret.get(id='string')

if res.rest_secret is not None:
    # handle response
    pass
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
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.rest_secret.update(id='string', rest_secret=components.RestSecret(
    id='<ID>',
    secret_type=components.SecretType.CREDENTIALS,
))

if res.rest_secret is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique ID                                                            |
| `rest_secret`                                                        | [Optional[components.RestSecret]](../../models/shared/restsecret.md) | :heavy_minus_sign:                                                   | RestSecret object to be updated                                      |


### Response

**[operations.UpdateRestSecretResponse](../../models/operations/updaterestsecretresponse.md)**

