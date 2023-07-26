# container

### Available Operations

* [get](#get) - Get details for a single container on the edge host. Add stream=true to get a stream instead.

## get

Get details for a single container on the edge host. Add stream=true to get a stream instead.

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetContainerRequest(
    id='0672d1ad-879e-4eb9-a65b-85efbd02bae0',
)

res = s.container.get(req)

if res.containers is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetContainerRequest](../../models/operations/getcontainerrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetContainerResponse](../../models/operations/getcontainerresponse.md)**

