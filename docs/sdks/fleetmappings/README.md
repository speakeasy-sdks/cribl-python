# FleetMappings
(*fleet_mappings*)

### Available Operations

* [get](#get) - Get a list of MappingRuleset objects

## get

Get a list of MappingRuleset objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.fleet_mappings.get()

if res.mapping_rulesets is not None:
    # handle response
    pass

```


### Response

**[operations.GetFleetMappingsResponse](../../models/operations/getfleetmappingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
