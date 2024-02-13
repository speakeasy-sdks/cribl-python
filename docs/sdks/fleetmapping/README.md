# FleetMapping
(*fleet_mapping*)

### Available Operations

* [create](#create) - Create MappingRuleset

## create

Create MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.MappingRuleset(
    id='<ID>',
)

res = s.fleet_mapping.create(req)

if res.mapping_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.MappingRuleset](../../models/components/mappingruleset.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateFleetMappingResponse](../../models/operations/createfleetmappingresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
