# ui_state

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

req = operations.GetUIStateRequest(
    key='eveniet',
)

res = s.ui_state.get(req)

if res.ui_states is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetUIStateRequest](../../models/operations/getuistaterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


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

req = operations.UpdateUIStateRequest(
    ui_state_patch=shared.UIStatePatch(
        args={
            "unde": 'consequuntur',
            "laboriosam": 'iusto',
        },
        op=shared.UIStatePatchOp.PUSH_RECENT,
        value='dignissimos',
    ),
    key='ab',
)

res = s.ui_state.update(req)

if res.ui_states is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateUIStateRequest](../../models/operations/updateuistaterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateUIStateResponse](../../models/operations/updateuistateresponse.md)**

