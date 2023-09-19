# ConfigGroup

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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ConfigGroup(
    config_version='similique',
    description='alias',
    estimated_ingest_rate=872651,
    git=shared.ConfigGroupGit(
        commit='quaerat',
        local_changes=273542,
        log=[
            shared.Commit(
                author_email='vel',
                author_name='quod',
                date_='officiis',
                hash='qui',
                message='dolorum',
                short='a',
            ),
        ],
    ),
    id='7a73cf3b-e453-4f87-8b32-6b5a73429cdb',
    inherits='dicta',
    is_fleet=False,
    is_search=False,
    name='Felix Gorczany',
    on_prem=False,
    provisioned=False,
    source_group_id='distinctio',
    tags='facilis',
    worker_count=396060,
    worker_remote_access=False,
)

res = s.config_group.create(req)

if res.config_group is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.config_group.delete(id='quam')

if res.config_group is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.config_group.get(id='molestias', fields_='temporibus')

if res.config_group is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.config_group.update(id='qui', config_group=shared.ConfigGroup(
    config_version='neque',
    description='fugit',
    estimated_ingest_rate=164959,
    git=shared.ConfigGroupGit(
        commit='odio',
        local_changes=124833,
        log=[
            shared.Commit(
                author_email='ullam',
                author_name='nam',
                date_='hic',
                hash='voluptatem',
                message='cumque',
                short='soluta',
            ),
        ],
    ),
    id='b1e31b8b-90f3-4443-a110-8e0adcf4b921',
    inherits='laudantium',
    is_fleet=False,
    is_search=False,
    name='Toni Wolff',
    on_prem=False,
    provisioned=False,
    source_group_id='omnis',
    tags='quis',
    worker_count=218403,
    worker_remote_access=False,
))

if res.config_group is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | Unique ID                                                          |
| `config_group`                                                     | [Optional[shared.ConfigGroup]](../../models/shared/configgroup.md) | :heavy_minus_sign:                                                 | ConfigGroup object to be updated                                   |


### Response

**[operations.UpdateConfigGroupResponse](../../models/operations/updateconfiggroupresponse.md)**

