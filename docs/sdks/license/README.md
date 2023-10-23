# License
(*license*)

### Available Operations

* [create](#create) - Create License
* [delete](#delete) - Delete License
* [get](#get) - Get License by ID

## create

Create License

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.License(
    cls=shared.LicenseCls.TRIAL,
    email='Loyal.Stokes@yahoo.com',
    exp=134365,
    f_ph=786546,
    f_phg=69025,
    guid='string',
    iat=996706,
    id='<ID>',
    iss='string',
    license='string',
    limits={
        "key": 'string',
    },
    quota=796474,
    title='string',
)

res = s.license.create(req)

if res.license is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [shared.License](../../models/shared/license.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.CreateLicenseResponse](../../models/operations/createlicenseresponse.md)**


## delete

Delete License

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.license.delete(id='string')

if res.license is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteLicenseResponse](../../models/operations/deletelicenseresponse.md)**


## get

Get License by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.license.get(id='string')

if res.license is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetLicenseResponse](../../models/operations/getlicenseresponse.md)**

