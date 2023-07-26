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
    config_version='optio',
    description='occaecati',
    estimated_ingest_rate=364544,
    git=shared.ConfigGroupGit(
        commit='voluptate',
        local_changes=501063,
        log=[
            shared.Commit(
                author_email='voluptas',
                author_name='numquam',
                date_='nemo',
                hash='quos',
                message='eius',
                short='aspernatur',
            ),
            shared.Commit(
                author_email='ducimus',
                author_name='nesciunt',
                date_='fuga',
                hash='laudantium',
                message='incidunt',
                short='quasi',
            ),
            shared.Commit(
                author_email='rem',
                author_name='fugiat',
                date_='dicta',
                hash='nisi',
                message='consequuntur',
                short='consectetur',
            ),
        ],
    ),
    id='09fb0929-921a-4efb-9f58-c4d86e68e4be',
    inherits='voluptatem',
    is_fleet=False,
    is_search=False,
    name='Mrs. Gina Abbott',
    on_prem=False,
    provisioned=False,
    source_group_id='enim',
    tags='sint',
    worker_count=858778,
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

req = operations.DeleteConfigGroupRequest(
    id='a757a59e-cfef-466e-b1ca-a3383c2beb47',
)

res = s.config_group.delete(req)

if res.config_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteConfigGroupRequest](../../models/operations/deleteconfiggrouprequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


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

req = operations.GetConfigGroupRequest(
    fields_='voluptate',
    id='373c8d72-f64d-41db-9f2c-4310661e9634',
)

res = s.config_group.get(req)

if res.config_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetConfigGroupRequest](../../models/operations/getconfiggrouprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


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

req = operations.UpdateConfigGroupRequest(
    config_group=shared.ConfigGroup(
        config_version='perspiciatis',
        description='earum',
        estimated_ingest_rate=117525,
        git=shared.ConfigGroupGit(
            commit='impedit',
            local_changes=975884,
            log=[
                shared.Commit(
                    author_email='itaque',
                    author_name='alias',
                    date_='nisi',
                    hash='itaque',
                    message='velit',
                    short='laborum',
                ),
                shared.Commit(
                    author_email='non',
                    author_name='dolor',
                    date_='iusto',
                    hash='sit',
                    message='doloremque',
                    short='consequatur',
                ),
                shared.Commit(
                    author_email='officia',
                    author_name='recusandae',
                    date_='ea',
                    hash='quidem',
                    message='voluptas',
                    short='facilis',
                ),
            ],
        ),
        id='c9b8f759-eac5-45a9-b41d-311352965bb8',
        inherits='dolorum',
        is_fleet=False,
        is_search=False,
        name='Beverly Abbott',
        on_prem=False,
        provisioned=False,
        source_group_id='quae',
        tags='quae',
        worker_count=264333,
        worker_remote_access=False,
    ),
    id='35e139db-c225-49b1-abda-8c070e1084cb',
)

res = s.config_group.update(req)

if res.config_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateConfigGroupRequest](../../models/operations/updateconfiggrouprequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateConfigGroupResponse](../../models/operations/updateconfiggroupresponse.md)**

