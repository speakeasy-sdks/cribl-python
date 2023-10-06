# Container
(*container*)

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


res = s.container.get(id='female')

if res.containers is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetContainerResponse](../../models/operations/getcontainerresponse.md)**

