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
    bearer_auth="",
)


res = s.destination_queue.delete(id='string')

if res.delete_destination_queue_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.DeleteDestinationQueueResponse](../../models/operations/deletedestinationqueueresponse.md)**

