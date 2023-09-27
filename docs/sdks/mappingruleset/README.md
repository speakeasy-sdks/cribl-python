# MappingRuleset
(*mapping_ruleset*)

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
                "inventore": 'deleniti',
            },
        ],
    ),
    id='14301042-1813-4d52-88ec-e7e253b66845',
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


res = s.mapping_ruleset.delete(id='ab')

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.mapping_ruleset.get(id='porro')

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


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


res = s.mapping_ruleset.update(id='autem', mapping_ruleset=shared.MappingRuleset(
    active=False,
    conf=shared.MappingRulesetConf(
        functions=[
            {
                "nobis": 'laboriosam',
            },
        ],
    ),
    id='e205e16d-eab3-4fec-9578-a64584273a84',
))

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique ID                                                                |
| `mapping_ruleset`                                                        | [Optional[shared.MappingRuleset]](../../models/shared/mappingruleset.md) | :heavy_minus_sign:                                                       | MappingRuleset object to be updated                                      |


### Response

**[operations.UpdateMappingRulesetResponse](../../models/operations/updatemappingrulesetresponse.md)**

