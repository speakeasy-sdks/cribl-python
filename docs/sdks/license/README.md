# license

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.License(
    cls=shared.LicenseCls.TRIAL,
    email='Bridie_DAmore17@hotmail.com',
    exp=27653,
    f_ph=838176,
    f_phg=660339,
    guid='quae',
    iat=414439,
    id='fc2b271a-289c-457e-854e-90439d222465',
    iss='vel',
    license='cupiditate',
    limits={
        "nisi": 'explicabo',
        "modi": 'doloremque',
    },
    quota=486944,
    title='Mr.',
)

res = s.license.create(req)

if res.license is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteLicenseRequest(
    id='84f7ab37-cef0-4222-9194-db55410adc66',
)

res = s.license.delete(req)

if res.license is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteLicenseRequest](../../models/operations/deletelicenserequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteLicenseResponse](../../models/operations/deletelicenseresponse.md)**


## get

Get License by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetLicenseRequest(
    id='9af90a26-c7cd-4c98-9f06-8981d6bb33cf',
)

res = s.license.get(req)

if res.license is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetLicenseRequest](../../models/operations/getlicenserequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetLicenseResponse](../../models/operations/getlicenseresponse.md)**

