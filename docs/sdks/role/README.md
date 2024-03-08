# Role
(*role*)

### Available Operations

* [create](#create) - Create Role
* [delete](#delete) - Delete Role
* [get](#get) - Get Role by ID
* [update](#update) - Update Role

## create

Create Role

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.Role(
    id='<id>',
    policy=[
        '<value>',
    ],
)

res = s.role.create(req)

if res.roles is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [components.Role](../../models/components/role.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.CreateRoleResponse](../../models/operations/createroleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete Role

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.role.delete(id='<value>')

if res.roles is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteRoleResponse](../../models/operations/deleteroleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get Role by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.role.get(id='<value>')

if res.roles is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetRoleResponse](../../models/operations/getroleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update Role

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.role.update(id='<value>', role=components.Role(
    id='<id>',
    policy=[
        '<value>',
    ],
))

if res.roles is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique ID                                                    |
| `role`                                                       | [Optional[components.Role]](../../models/components/role.md) | :heavy_minus_sign:                                           | Role object to be updated                                    |


### Response

**[operations.UpdateRoleResponse](../../models/operations/updateroleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
