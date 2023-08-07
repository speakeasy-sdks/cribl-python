# config_group

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
    config_version='voluptatibus',
    description='molestias',
    estimated_ingest_rate=889794,
    git=shared.ConfigGroupGit(
        commit='sapiente',
        local_changes=764562,
        log=[
            shared.Commit(
                author_email='rerum',
                author_name='tempora',
                date_='quis',
                hash='inventore',
                message='fugit',
                short='cumque',
            ),
        ],
    ),
    id='1032648d-c2f6-4151-99eb-fd0e9fe6c632',
    inherits='cumque',
    is_fleet=False,
    is_search=False,
    name='Philip O'Kon',
    on_prem=False,
    provisioned=False,
    source_group_id='consequatur',
    tags='quasi',
    worker_count=90233,
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


res = s.config_group.delete(id='ducimus')

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


res = s.config_group.get(id='natus', fields_='occaecati')

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


res = s.config_group.update(id='suscipit', config_group=shared.ConfigGroup(
    config_version='adipisci',
    description='quasi',
    estimated_ingest_rate=169025,
    git=shared.ConfigGroupGit(
        commit='doloribus',
        local_changes=859581,
        log=[
            shared.Commit(
                author_email='ipsa',
                author_name='tempora',
                date_='nihil',
                hash='molestiae',
                message='dicta',
                short='iusto',
            ),
            shared.Commit(
                author_email='esse',
                author_name='praesentium',
                date_='maiores',
                hash='reiciendis',
                message='vel',
                short='architecto',
            ),
            shared.Commit(
                author_email='fugiat',
                author_name='doloremque',
                date_='dicta',
                hash='odio',
                message='tempora',
                short='esse',
            ),
            shared.Commit(
                author_email='ex',
                author_name='consectetur',
                date_='aliquid',
                hash='ipsa',
                message='laborum',
                short='sunt',
            ),
        ],
    ),
    id='5db6a660-659a-41ad-aaab-5851d6c645b0',
    inherits='molestias',
    is_fleet=False,
    is_search=False,
    name='Gene Brekke',
    on_prem=False,
    provisioned=False,
    source_group_id='veritatis',
    tags='rerum',
    worker_count=665678,
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

