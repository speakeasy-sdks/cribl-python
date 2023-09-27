# Certificate
(*certificate*)

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
    ca='omnis',
    cert='facilis',
    description='perspiciatis',
    id='0c28909b-3fe4-49a8-99cb-f48633323f9b',
    in_use=[
        'voluptate',
    ],
    passphrase='dignissimos',
    priv_key='reiciendis',
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


res = s.certificate.delete(id='amet')

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


res = s.certificate.get(id='dolorum')

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


res = s.certificate.update(id='numquam', certificate=shared.Certificate(
    ca='veritatis',
    cert='ipsa',
    description='ipsa',
    id='674ebf69-280d-41ba-b7a8-9ebf737ae420',
    in_use=[
        'amet',
    ],
    passphrase='optio',
    priv_key='accusamus',
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

