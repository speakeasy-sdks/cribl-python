# License

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
    cls=shared.LicenseCls.FREE,
    email='Felipe_King63@hotmail.com',
    exp=672041,
    f_ph=813054,
    f_phg=266697,
    guid='voluptatibus',
    iat=564064,
    id='efc1b451-2c10-4326-88dc-2f615199ebfd',
    iss='eaque',
    license='earum',
    limits={
        "perspiciatis": 'maiores',
    },
    quota=891801,
    title='Mrs.',
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


res = s.license.delete(id='porro')

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


res = s.license.get(id='suscipit')

if res.license is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetLicenseResponse](../../models/operations/getlicenseresponse.md)**

