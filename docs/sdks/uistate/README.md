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
    bearer_auth="",
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


## update

Update UI state by key

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.ui_state.update(key='string', ui_state_patch=shared.UIStatePatch(
    args={
        "key": 'string',
    },
    op=shared.UIStatePatchOp.PUSH_RECENT,
    value='string',
))

if res.ui_states is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `key`                                                                | *str*                                                                | :heavy_check_mark:                                                   | UI state key                                                         |
| `ui_state_patch`                                                     | [Optional[shared.UIStatePatch]](../../models/shared/uistatepatch.md) | :heavy_minus_sign:                                                   | UI State Patch object                                                |


### Response

**[operations.UpdateUIStateResponse](../../models/operations/updateuistateresponse.md)**

