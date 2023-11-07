# Certificate
(*.certificate*)

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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.Certificate(
    cert='string',
    id='<ID>',
    in_use=[
        'string',
    ],
    priv_key='string',
)

res = s.certificate.create(req)

if res.certificate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.Certificate](../../models/shared/certificate.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateCertificateResponse](../../models/operations/createcertificateresponse.md)**


## delete

Delete Certificate

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.certificate.delete(id='string')

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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.certificate.get(id='string')

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
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.certificate.update(id='string', certificate=components.Certificate(
    cert='string',
    id='<ID>',
    in_use=[
        'string',
    ],
    priv_key='string',
))

if res.certificate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique ID                                                              |
| `certificate`                                                          | [Optional[components.Certificate]](../../models/shared/certificate.md) | :heavy_minus_sign:                                                     | Certificate object to be updated                                       |


### Response

**[operations.UpdateCertificateResponse](../../models/operations/updatecertificateresponse.md)**

