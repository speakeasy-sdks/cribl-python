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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.PolicyRule(
    args=[
        'sit',
    ],
    description='iusto',
    id='0e1084cb-0672-4d1a-9879-eeb9665b85ef',
    template=[
        'cum',
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.policy_rule.delete(id='at')

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.policy_rule.get(id='alias')

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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.policy_rule.update(id='quia', policy_rule=shared.PolicyRule(
    args=[
        'quidem',
    ],
    description='fuga',
    id='e0be2d78-2259-4e3e-a4b5-197f92443da7',
    template=[
        'optio',
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

