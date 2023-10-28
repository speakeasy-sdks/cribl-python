# OutputStatusID
(*output_status_id*)

### Available Operations

* [get](#get) - Get OutputStatus by ID

## get

Get OutputStatus by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.output_status_id.get(id='string')

if res.output_statuses is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetOutputStatusIDResponse](../../models/operations/getoutputstatusidresponse.md)**

