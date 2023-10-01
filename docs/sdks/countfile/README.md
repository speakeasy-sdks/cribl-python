# CountFile
(*count_file*)

### Available Operations

* [get](#get) - get the count of files of changed

## get

get the count of files of changed

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.count_file.get(group='female')

if res.count_file is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group`            | *Optional[str]*    | :heavy_minus_sign: | Group ID           |


### Response

**[operations.GetCountFileResponse](../../models/operations/getcountfileresponse.md)**

