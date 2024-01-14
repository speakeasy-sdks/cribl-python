# UIState
(*ui_state*)

### Available Operations

* [get](#get) - Get UI state by key
* [update](#update) - Update UI state by key

## get

Get UI state by key

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ui_state.get(key='string')

if res.ui_states is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *str*              | :heavy_check_mark: | UI state key       |


### Response

**[operations.GetUIStateResponse](../../models/operations/getuistateresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update UI state by key

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.ui_state.update(key='string', ui_state_patch=components.UIStatePatch(
    args={
        'key': 'string',
    },
    op=components.UIStatePatchOp.PUSH_RECENT,
    value='string',
))

if res.ui_states is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `key`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | UI state key                                                                 |
| `ui_state_patch`                                                             | [Optional[components.UIStatePatch]](../../models/components/uistatepatch.md) | :heavy_minus_sign:                                                           | UI State Patch object                                                        |


### Response

**[operations.UpdateUIStateResponse](../../models/operations/updateuistateresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
