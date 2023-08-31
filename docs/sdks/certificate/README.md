# certificate

### Available Operations

* [create](#create) - Create Certificate
* [delete](#delete) - Delete Certificate
* [get](#get) - Get Certificate by ID
* [update](#update) - Update Certificate

## create

Create Certificate

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.Certificate(
    ca='eveniet',
    cert='occaecati',
    description='consequuntur',
    id='2a57a15b-e3e0-4608-87e2-b6e3ab8845f0',
    in_use=[
        'perspiciatis',
        'nihil',
    ],
    passphrase='mollitia',
    priv_key='voluptas',
)

res = s.certificate.create(req)

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.Certificate](../../models/shared/certificate.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateCertificateResponse](../../models/operations/createcertificateresponse.md)**


## delete

Delete Certificate

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.certificate.delete(id='alias')

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteCertificateResponse](../../models/operations/deletecertificateresponse.md)**


## get

Get Certificate by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.certificate.get(id='maiores')

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetCertificateResponse](../../models/operations/getcertificateresponse.md)**


## update

Update Certificate

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.certificate.update(id='reiciendis', certificate=shared.Certificate(
    ca='dolores',
    cert='id',
    description='minima',
    id='4a31e947-64a3-4e86-9e79-56f9251a5a9d',
    in_use=[
        'ex',
        'aliquid',
        'accusantium',
    ],
    passphrase='repellat',
    priv_key='doloribus',
))

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Unique ID                                                          |
| `certificate`                                                      | [Optional[shared.Certificate]](../../models/shared/certificate.md) | :heavy_minus_sign:                                                 | Certificate object to be updated                                   |


### Response

**[operations.UpdateCertificateResponse](../../models/operations/updatecertificateresponse.md)**

