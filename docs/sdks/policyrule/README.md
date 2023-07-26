# policy_rule

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
        'fugit',
        'repudiandae',
        'vitae',
        'consequatur',
    ],
    description='nemo',
    id='944b935d-237a-472f-9084-9d6aed4aecb7',
    template=[
        'neque',
        'esse',
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

req = operations.DeletePolicyRuleRequest(
    id='cd9222c9-ff57-4491-aabf-a2e761f0ca4d',
)

res = s.policy_rule.delete(req)

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeletePolicyRuleRequest](../../models/operations/deletepolicyrulerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


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

req = operations.GetPolicyRuleRequest(
    id='456ef103-1e68-499f-8c20-01e22cd55cc0',
)

res = s.policy_rule.get(req)

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetPolicyRuleRequest](../../models/operations/getpolicyrulerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


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

req = operations.UpdatePolicyRuleRequest(
    policy_rule=shared.PolicyRule(
        args=[
            'molestias',
            'modi',
        ],
        description='similique',
        id='184d76d9-71fc-4820-865b-037bb8e0cc88',
        template=[
            'veritatis',
            'quas',
        ],
    ),
    id='7e4de04a-f28c-45dd-9b46-aa1cfd6d828d',
)

res = s.policy_rule.update(req)

if res.policy_rules is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdatePolicyRuleRequest](../../models/operations/updatepolicyrulerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdatePolicyRuleResponse](../../models/operations/updatepolicyruleresponse.md)**

