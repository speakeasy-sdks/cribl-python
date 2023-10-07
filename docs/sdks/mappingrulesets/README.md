# MappingRulesets
(*mapping_rulesets*)

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


res = s.mapping_rulesets.delete(id='program')

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


res = s.mapping_rulesets.update(id='Van', request_body={
    "East": 'male',
})

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `id`                                | *str*                               | :heavy_check_mark:                  | Unique ID                           |
| `request_body`                      | dict[str, *Any*]                    | :heavy_minus_sign:                  | MappingRuleset object to be updated |


### Response

**[operations.UpdateMappingRulesetsResponse](../../models/operations/updatemappingrulesetsresponse.md)**

