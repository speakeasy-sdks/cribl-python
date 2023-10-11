# PolicyRule
(*policy_rule*)

### Available Operations

* [create](#create) - Create PolicyRule
* [delete](#delete) - Delete PolicyRule
* [get](#get) - Get PolicyRule by ID
* [update](#update) - Update PolicyRule

## create

Create PolicyRule

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.PolicyRule(
    args=[
        'online',
    ],
    id='<ID>',
    template=[
        'Configuration',
    ],
)

res = s.policy_rule.create(req)

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.PolicyRule](../../models/shared/policyrule.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreatePolicyRuleResponse](../../models/operations/createpolicyruleresponse.md)**


## delete

Delete PolicyRule

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.policy_rule.delete(id='program')

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeletePolicyRuleResponse](../../models/operations/deletepolicyruleresponse.md)**


## get

Get PolicyRule by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.policy_rule.get(id='female')

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetPolicyRuleResponse](../../models/operations/getpolicyruleresponse.md)**


## update

Update PolicyRule

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.policy_rule.update(id='Van', policy_rule=shared.PolicyRule(
    args=[
        'East',
    ],
    id='<ID>',
    template=[
        'male',
    ],
))

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Unique ID                                                        |
| `policy_rule`                                                    | [Optional[shared.PolicyRule]](../../models/shared/policyrule.md) | :heavy_minus_sign:                                               | PolicyRule object to be updated                                  |


### Response

**[operations.UpdatePolicyRuleResponse](../../models/operations/updatepolicyruleresponse.md)**

