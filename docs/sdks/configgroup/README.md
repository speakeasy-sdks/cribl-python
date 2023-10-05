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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ConfigGroup(
    config_version='bluetooth Extended',
    description='Customer-focused regional approach',
    estimated_ingest_rate=996706,
    git=shared.ConfigGroupGit(
        commit='abnormally deposit evolve',
        local_changes=715040,
        log=[
            shared.Commit(
                author_email='SUV quantify Polestar',
                author_name='physical Ameliorated',
                date_='after',
                hash='Intelligent Fish',
                message='Fiat',
                short='Grocery Borders Northwest',
            ),
        ],
    ),
    id='<ID>',
    inherits='Kentucky animated',
    is_fleet=False,
    is_search=False,
    name='Interactions Senior Mouse',
    on_prem=False,
    provisioned=False,
    source_group_id='or',
    tags='Edinburg Investor',
    worker_count=550483,
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


res = s.config_group.delete(id='program')

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


res = s.config_group.get(id='female', fields_='program')

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


res = s.config_group.update(id='Van', config_group=shared.ConfigGroup(
    config_version='Reactive',
    description='Vision-oriented didactic migration',
    estimated_ingest_rate=684199,
    git=shared.ConfigGroupGit(
        commit='invoice Arizona',
        local_changes=278281,
        log=[
            shared.Commit(
                author_email='online dynamic white',
                author_name='Carolina syndicate',
                date_='implement JBOD',
                hash='Quality guestbook driver',
                message='pascal Gasoline',
                short='Northeast Wooden',
            ),
        ],
    ),
    id='<ID>',
    inherits='Jaguar Dodge',
    is_fleet=False,
    is_search=False,
    name='Buckinghamshire frictionless haptic',
    on_prem=False,
    provisioned=False,
    source_group_id='possimus navigating Diesel',
    tags='Greens',
    worker_count=656776,
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

