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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.License(
    cls=shared.LicenseCls.TRIAL,
    email='Elliott.Hammes36@yahoo.com',
    exp=597303,
    f_ph=470649,
    f_phg=649078,
    guid='voluptas',
    iat=5189,
    id='ff2a54a3-1e94-4764-a3e8-65e7956f9251',
    iss='animi',
    license='nostrum',
    limits={
        "mollitia": 'provident',
    },
    quota=821719,
    title='Miss',
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


res = s.license.delete(id='ex')

if res.license is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.license.get(id='aliquid')

if res.license is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetLicenseResponse](../../models/operations/getlicenseresponse.md)**

