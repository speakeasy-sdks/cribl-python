# MappingRulesetID
(*mapping_ruleset_id*)

### Available Operations

* [get](#get) - Get MappingRuleset by ID

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


res = s.mapping_ruleset_id.get(id='quasi')

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetMappingRulesetIDResponse](../../models/operations/getmappingrulesetidresponse.md)**

