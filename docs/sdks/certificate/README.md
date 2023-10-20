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
    bearer_auth="",
)

req = shared.Certificate(
    cert='online',
    id='<ID>',
    in_use=[
        'Configuration',
    ],
    priv_key='Money',
)

res = s.certificate.create(req)

if res.certificate is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.certificate.delete(id='program')

if res.certificate is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.certificate.get(id='female')

if res.certificate is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.certificate.update(id='Van', certificate=shared.Certificate(
    cert='East',
    id='<ID>',
    in_use=[
        'male',
    ],
    priv_key='Metal',
))

if res.certificate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Unique ID                                                          |
| `certificate`                                                      | [Optional[shared.Certificate]](../../models/shared/certificate.md) | :heavy_minus_sign:                                                 | Certificate object to be updated                                   |


### Response

**[operations.UpdateCertificateResponse](../../models/operations/updatecertificateresponse.md)**

