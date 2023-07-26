# field_summaries

### Available Operations

* [get](#get) - List field summaries

## get

List field summaries

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetFieldSummariesRequest(
    id='418e3bb9-1c8d-4975-a0e8-419d8f84f144',
)

res = s.field_summaries.get(req)

if res.field_summaries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetFieldSummariesRequest](../../models/operations/getfieldsummariesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetFieldSummariesResponse](../../models/operations/getfieldsummariesresponse.md)**

