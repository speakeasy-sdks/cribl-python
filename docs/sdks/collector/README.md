# collector

### Available Operations

* [get](#get) - Get Collector by ID

## get

Get Collector by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetCollectorRequest(
    id='350d8cdb-5a34-4181-8301-0421813d5208',
)

res = s.collector.get(req)

if res.collectors is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetCollectorRequest](../../models/operations/getcollectorrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetCollectorResponse](../../models/operations/getcollectorresponse.md)**

