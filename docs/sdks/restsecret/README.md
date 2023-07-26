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
    api_key='molestiae',
    description='aliquid',
    id='76334254-038b-4fb5-971e-98190557389c',
    password='itaque',
    secret_key='at',
    secret_type=shared.SecretType.CREDENTIALS,
    tags='id',
    username='Oceane_Kirlin63',
    value='dolor',
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

req = operations.DeleteRestSecretRequest(
    id='9594d66b-c2ae-4480-a32b-9954b6fa2206',
)

res = s.rest_secret.delete(req)

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteRestSecretRequest](../../models/operations/deleterestsecretrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


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

req = operations.GetRestSecretRequest(
    id='36982855-3cb1-4000-abef-4921ec2053b7',
)

res = s.rest_secret.get(req)

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetRestSecretRequest](../../models/operations/getrestsecretrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


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

req = operations.UpdateRestSecretRequest(
    rest_secret=shared.RestSecret(
        api_key='eius',
        description='perspiciatis',
        id='366ac8ee-0f2b-4f19-988d-40d03f3deba2',
        password='natus',
        secret_key='molestiae',
        secret_type=shared.SecretType.CREDENTIALS,
        tags='earum',
        username='Cruz.Watsica',
        value='harum',
    ),
    id='c40df868-fd52-4405-8b33-1d492f4f127f',
)

res = s.rest_secret.update(req)

if res.rest_secret is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateRestSecretRequest](../../models/operations/updaterestsecretrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateRestSecretResponse](../../models/operations/updaterestsecretresponse.md)**

