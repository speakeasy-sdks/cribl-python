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

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_rulesets.delete(id='string')

if res.mapping_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteMappingRulesetsResponse](../../models/operations/deletemappingrulesetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get a list of MappingRuleset objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_rulesets.get()

if res.mapping_rulesets is not None:
    # handle response
    pass
```


### Response

**[operations.GetMappingRulesetsResponse](../../models/operations/getmappingrulesetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_rulesets.update(id='string', mapping_ruleset=components.MappingRuleset(
    id='<ID>',
))

if res.mapping_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | Unique ID                                                                        |
| `mapping_ruleset`                                                                | [Optional[components.MappingRuleset]](../../models/components/mappingruleset.md) | :heavy_minus_sign:                                                               | MappingRuleset object to be updated                                              |


### Response

**[operations.UpdateMappingRulesetsResponse](../../models/operations/updatemappingrulesetsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
