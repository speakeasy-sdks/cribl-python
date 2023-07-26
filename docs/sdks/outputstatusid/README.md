# output_status_id

### Available Operations

* [get](#get) - Get OutputStatus by ID

## get

Get OutputStatus by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetOutputStatusIDRequest(
    id='82cb70f8-cfd5-4fb6-a91b-9a9f74846e2c',
)

res = s.output_status_id.get(req)

if res.output_statuses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetOutputStatusIDRequest](../../models/operations/getoutputstatusidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetOutputStatusIDResponse](../../models/operations/getoutputstatusidresponse.md)**

