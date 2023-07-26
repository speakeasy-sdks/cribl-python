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
                "dignissimos": 'libero',
                "illo": 'ab',
            },
            {
                "accusamus": 'saepe',
                "tempore": 'veniam',
            },
            {
                "reiciendis": 'earum',
            },
            {
                "praesentium": 'nemo',
                "repellat": 'quisquam',
            },
        ],
    ),
    id='37814d4c-98e0-4c2b-b89e-b75dad636c60',
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

