# mapping_ruleset_id

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

req = operations.GetMappingRulesetIDRequest(
    id='96ff3c57-4750-4135-be44-f51f8b084c31',
)

res = s.mapping_ruleset_id.get(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMappingRulesetIDRequest](../../models/operations/getmappingrulesetidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetMappingRulesetIDResponse](../../models/operations/getmappingrulesetidresponse.md)**

