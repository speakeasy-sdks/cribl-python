# role

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.Role(
    id='b0e0bf1f-8217-4978-90ac-ca77aeb7b702',
    policy=[
        'est',
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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteRoleRequest(
    id='52046b64-e99f-4b0e-a7e0-94fdfed5540e',
)

res = s.role.delete(req)

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteRoleRequest](../../models/operations/deleterolerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteRoleResponse](../../models/operations/deleteroleresponse.md)**


## get

Get Role by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetRoleRequest(
    id='f53a34a1-b8fe-4997-b1ad-c05d85ae2dfb',
)

res = s.role.get(req)

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetRoleRequest](../../models/operations/getrolerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetRoleResponse](../../models/operations/getroleresponse.md)**


## update

Update Role

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateRoleRequest(
    role=shared.Role(
        id='70fb3874-290d-4336-961e-ca16ef89451b',
        policy=[
            'ducimus',
            'nisi',
            'accusamus',
            'officiis',
        ],
    ),
    id='eb518c4d-a1fa-4d35-912f-06d4e5b72f0f',
)

res = s.role.update(req)

if res.roles is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateRoleRequest](../../models/operations/updaterolerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateRoleResponse](../../models/operations/updateroleresponse.md)**

