# FleetMappings
(*fleet_mappings*)

### Available Operations

* [get](#get) - Get a list of MappingRuleset objects

## get

Get a list of MappingRuleset objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.fleet_mappings.get()

if res.mapping_rulesets is not None:
    # handle response
    pass
```


### Response

**[operations.GetFleetMappingsResponse](../../models/operations/getfleetmappingsresponse.md)**

