# destination_queue

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

req = operations.DeleteDestinationQueueRequest(
    id='aea4c506-a8aa-494c-8264-4cf5e9d9a457',
)

res = s.destination_queue.delete(req)

if res.delete_destination_queue_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteDestinationQueueRequest](../../models/operations/deletedestinationqueuerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteDestinationQueueResponse](../../models/operations/deletedestinationqueueresponse.md)**

