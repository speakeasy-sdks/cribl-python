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
    ca='aliquam',
    cert='ad',
    description='repellat',
    id='0597a60f-f2a5-44a3-9e94-764a3e865e79',
    in_use=[
        'eum',
        'reiciendis',
    ],
    passphrase='provident',
    priv_key='aspernatur',
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

req = operations.DeleteCertificateRequest(
    id='51a5a9da-660f-4f57-bfaa-d4f9efc1b451',
)

res = s.certificate.delete(req)

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteCertificateRequest](../../models/operations/deletecertificaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


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

req = operations.GetCertificateRequest(
    id='2c103264-8dc2-4f61-9199-ebfd0e9fe6c6',
)

res = s.certificate.get(req)

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCertificateRequest](../../models/operations/getcertificaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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

req = operations.UpdateCertificateRequest(
    certificate=shared.Certificate(
        ca='dolorem',
        cert='fugit',
        description='cumque',
        id='a3aed011-7996-4312-bde0-4771778ff61d',
        in_use=[
            'dicta',
        ],
        passphrase='odio',
        priv_key='tempora',
    ),
    id='76360a15-db6a-4660-a59a-1adeaab5851d',
)

res = s.certificate.update(req)

if res.certificate is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCertificateRequest](../../models/operations/updatecertificaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateCertificateResponse](../../models/operations/updatecertificateresponse.md)**

