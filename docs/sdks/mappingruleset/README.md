# mapping_ruleset

### Available Operations

* [create](#create) - Create MappingRuleset
* [delete](#delete) - Delete MappingRuleset
* [get](#get) - Get MappingRuleset by ID
* [update](#update) - Update MappingRuleset

## create

Create MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.MappingRuleset(
    active=False,
    conf=shared.MappingRulesetConf(
        functions=[
            {
                "voluptate": 'tempore',
                "in": 'omnis',
                "possimus": 'tenetur',
                "recusandae": 'expedita',
            },
            {
                "esse": 'harum',
                "ad": 'quod',
            },
            {
                "totam": 'vero',
            },
        ],
    ),
    id='4baf91e5-06ef-4890-a54b-475f16f56d38',
)

res = s.mapping_ruleset.create(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.MappingRuleset](../../models/shared/mappingruleset.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateMappingRulesetResponse](../../models/operations/createmappingrulesetresponse.md)**


## delete

Delete MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteMappingRulesetRequest(
    id='5a3c4ac6-31b9-49e2-aced-8f9fdb9410f6',
)

res = s.mapping_ruleset.delete(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeleteMappingRulesetRequest](../../models/operations/deletemappingrulesetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.DeleteMappingRulesetResponse](../../models/operations/deletemappingrulesetresponse.md)**


## get

Get MappingRuleset by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetMappingRulesetRequest(
    id='3bbf8178-37b0-41af-9d78-8624189eb448',
)

res = s.mapping_ruleset.get(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMappingRulesetRequest](../../models/operations/getmappingrulesetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetMappingRulesetResponse](../../models/operations/getmappingrulesetresponse.md)**


## update

Update MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateMappingRulesetRequest(
    mapping_ruleset=shared.MappingRuleset(
        active=False,
        conf=shared.MappingRulesetConf(
            functions=[
                {
                    "sapiente": 'quis',
                },
                {
                    "ratione": 'consectetur',
                },
            ],
        ),
        id='f19dbf12-5ce4-4152-aab9-cd7e5224a6a0',
    ),
    id='e123b784-7ec5-49e1-b67f-3c4cce4b6d76',
)

res = s.mapping_ruleset.update(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateMappingRulesetRequest](../../models/operations/updatemappingrulesetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UpdateMappingRulesetResponse](../../models/operations/updatemappingrulesetresponse.md)**

