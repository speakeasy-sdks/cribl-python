# mapping_rulesets

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

req = operations.DeleteMappingRulesetsRequest(
    id='97e193a2-4546-47f9-8874-c2d5cc497223',
)

res = s.mapping_rulesets.delete(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteMappingRulesetsRequest](../../models/operations/deletemappingrulesetsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


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

req = operations.UpdateMappingRulesetsRequest(
    mapping_ruleset=shared.MappingRuleset(
        active=False,
        conf=shared.MappingRulesetConf(
            functions=[
                {
                    "iure": 'aliquid',
                    "cum": 'fugiat',
                    "rem": 'voluptatibus',
                    "officiis": 'corporis',
                },
            ],
        ),
        id='d00b979e-f203-4873-a059-0ccc10964003',
    ),
    id='13b3e504-4f65-4fe7-adc4-077d0cc3f408',
)

res = s.mapping_rulesets.update(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateMappingRulesetsRequest](../../models/operations/updatemappingrulesetsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.UpdateMappingRulesetsResponse](../../models/operations/updatemappingrulesetsresponse.md)**

