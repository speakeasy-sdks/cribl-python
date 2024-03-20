# MappingRulesetID
(*mapping_ruleset_id*)

### Available Operations

* [get](#get) - Get MappingRuleset by ID

## get

Get MappingRuleset by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_ruleset_id.get(id='<value>')

if res.mapping_rulesets is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetMappingRulesetIDResponse](../../models/operations/getmappingrulesetidresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
