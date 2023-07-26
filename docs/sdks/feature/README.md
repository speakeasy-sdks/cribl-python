# feature

### Available Operations

* [get](#get) - Get feature by Id

## get

Get feature by id (i.e. 'type/name`)

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetFeatureRequest(
    id='f9621a6a-4f77-4a87-ae3e-4be752c65b34',
)

res = s.feature.get(req)

if res.features_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetFeatureRequest](../../models/operations/getfeaturerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetFeatureResponse](../../models/operations/getfeatureresponse.md)**

