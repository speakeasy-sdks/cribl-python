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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
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
| errors.SDKError  | 400-600          | */*              |

## get

Get a list of MappingRuleset objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
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
| errors.SDKError  | 400-600          | */*              |

## update

Update MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.mapping_rulesets.update(id='string', mapping_ruleset=components.MappingRuleset(
    conf=components.Conf(
        functions=[
            {
                "key": 'string',
            },
        ],
    ),
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
| errors.SDKError  | 400-600          | */*              |
