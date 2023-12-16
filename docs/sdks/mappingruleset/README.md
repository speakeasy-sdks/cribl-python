# MappingRuleset
(*mapping_ruleset*)

### Available Operations

* [create](#create) - Create MappingRuleset
* [delete](#delete) - Delete MappingRuleset
* [get](#get) - Get MappingRuleset by ID
* [update](#update) - Update MappingRuleset

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
    conf=components.Conf(
        functions=[
            {
                'key': 'string',
            },
        ],
    ),
    id='<ID>',
)

res = s.mapping_ruleset.create(req)

if res.mapping_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.MappingRuleset](../../models/components/mappingruleset.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateMappingRulesetResponse](../../models/operations/createmappingrulesetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## delete

Delete MappingRuleset

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_ruleset.delete(id='string')

if res.mapping_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteMappingRulesetResponse](../../models/operations/deletemappingrulesetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get MappingRuleset by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_ruleset.get(id='string')

if res.mapping_rulesets is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetMappingRulesetResponse](../../models/operations/getmappingrulesetresponse.md)**
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
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.mapping_ruleset.update(id='string', mapping_ruleset=components.MappingRuleset(
    conf=components.Conf(
        functions=[
            {
                'key': 'string',
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

**[operations.UpdateMappingRulesetResponse](../../models/operations/updatemappingrulesetresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
