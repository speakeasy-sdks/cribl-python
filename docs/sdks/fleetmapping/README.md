# fleet_mapping

### Available Operations

* [create](#create) - Create MappingRuleset

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
                "saepe": 'consequatur',
            },
            {
                "debitis": 'facere',
                "quisquam": 'cumque',
            },
            {
                "dolorum": 'deserunt',
                "ad": 'reiciendis',
            },
            {
                "porro": 'laborum',
            },
        ],
    ),
    id='bd905a97-2e05-4672-8227-b2d309470bf7',
)

res = s.fleet_mapping.create(req)

if res.mapping_rulesets is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.MappingRuleset](../../models/shared/mappingruleset.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateFleetMappingResponse](../../models/operations/createfleetmappingresponse.md)**

