# ConfigGroup
(*config_group*)

### Available Operations

* [create](#create) - Create ConfigGroup
* [delete](#delete) - Delete ConfigGroup
* [get](#get) - Get a specific ConfigGroup object
* [update](#update) - Update ConfigGroup

## create

Create ConfigGroup

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.ConfigGroup(
    config_version='string',
    git=shared.ConfigGroupGit(
        log=[
            shared.Commit(
                date_='string',
                hash='string',
                message='string',
                short='string',
            ),
        ],
    ),
    id='<ID>',
)

res = s.config_group.create(req)

if res.config_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.ConfigGroup](../../models/shared/configgroup.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateConfigGroupResponse](../../models/operations/createconfiggroupresponse.md)**


## delete

Delete ConfigGroup

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.config_group.delete(id='string')

if res.config_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteConfigGroupResponse](../../models/operations/deleteconfiggroupresponse.md)**


## get

Get a specific ConfigGroup object

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.config_group.get(id='string', fields_='string')

if res.config_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | Unique ID                                                                               |
| `fields_`                                                                               | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | query string additional fields to add to results: git.commit, git.localChanges, git.log |


### Response

**[operations.GetConfigGroupResponse](../../models/operations/getconfiggroupresponse.md)**


## update

Update ConfigGroup

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.config_group.update(id='string', config_group=shared.ConfigGroup(
    config_version='string',
    git=shared.ConfigGroupGit(
        log=[
            shared.Commit(
                date_='string',
                hash='string',
                message='string',
                short='string',
            ),
        ],
    ),
    id='<ID>',
))

if res.config_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Unique ID                                                          |
| `config_group`                                                     | [Optional[shared.ConfigGroup]](../../models/shared/configgroup.md) | :heavy_minus_sign:                                                 | ConfigGroup object to be updated                                   |


### Response

**[operations.UpdateConfigGroupResponse](../../models/operations/updateconfiggroupresponse.md)**

