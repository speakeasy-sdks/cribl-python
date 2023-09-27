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
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.ui_state.get(key='amet')

if res.ui_states is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *str*              | :heavy_check_mark: | UI state key       |


### Response

**[operations.GetUIStateResponse](../../models/operations/getuistateresponse.md)**


## update

Update UI state by key

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.ui_state.update(key='laborum', ui_state_patch=shared.UIStatePatch(
    args={
        "modi": 'perferendis',
    },
    op=shared.UIStatePatchOp.PUSH_RECENT,
    value='architecto',
))

if res.ui_states is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `key`                                                                | *str*                                                                | :heavy_check_mark:                                                   | UI state key                                                         |
| `ui_state_patch`                                                     | [Optional[shared.UIStatePatch]](../../models/shared/uistatepatch.md) | :heavy_minus_sign:                                                   | UI State Patch object                                                |


### Response

**[operations.UpdateUIStateResponse](../../models/operations/updateuistateresponse.md)**

