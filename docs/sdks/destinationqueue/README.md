# DestinationQueue
(*destination_queue*)

### Available Operations

* [delete](#delete) - Delete destination persistent queue

## delete

Delete destination persistent queue

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.destination_queue.delete(id='program')

if res.delete_destination_queue_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.DeleteDestinationQueueResponse](../../models/operations/deletedestinationqueueresponse.md)**

