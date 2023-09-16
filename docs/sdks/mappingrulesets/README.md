# MappingRulesets

### Available Operations

* [delete](#delete) - Delete MappingRuleset
* [get](#get) - Get a list of MappingRuleset objects
* [update](#update) - Update MappingRuleset

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


res = s.mapping_rulesets.delete(id='iusto')

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteMappingRulesetsResponse](../../models/operations/deletemappingrulesetsresponse.md)**


## get

Get a list of MappingRuleset objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.mapping_rulesets.get()

if res.mapping_rulesets is not None:
    # handle response
```


### Response

**[operations.GetMappingRulesetsResponse](../../models/operations/getmappingrulesetsresponse.md)**


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


res = s.mapping_rulesets.update(id='sit', mapping_ruleset=shared.MappingRuleset(
    active=False,
    conf=shared.MappingRulesetConf(
        functions=[
            {
                "doloremque": 'consequatur',
            },
        ],
    ),
    id='ae6b6bc9-b8f7-459e-ac55-a9741d311352',
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

**[operations.UpdateMappingRulesetsResponse](../../models/operations/updatemappingrulesetsresponse.md)**

