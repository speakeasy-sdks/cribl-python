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
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.Role(
    id='<ID>',
    policy=[
        'online',
    ],
)

res = s.role.create(req)

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.Role](../../models/shared/role.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateRoleResponse](../../models/operations/createroleresponse.md)**


## delete

Delete Role

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.role.delete(id='program')

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteRoleResponse](../../models/operations/deleteroleresponse.md)**


## get

Get Role by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.role.get(id='female')

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetRoleResponse](../../models/operations/getroleresponse.md)**


## update

Update Role

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.role.update(id='Van', role=shared.Role(
    id='<ID>',
    policy=[
        'East',
    ],
))

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | Unique ID                                            |
| `role`                                               | [Optional[shared.Role]](../../models/shared/role.md) | :heavy_minus_sign:                                   | Role object to be updated                            |


### Response

**[operations.UpdateRoleResponse](../../models/operations/updateroleresponse.md)**

