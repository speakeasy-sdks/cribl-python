# DestinationQueue
(*destination_queue*)

### Available Operations

* [delete](#delete) - Delete destination persistent queue

## delete

Delete destination persistent queue

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.destination_queue.delete(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.DeleteDestinationQueueResponse](../../models/operations/deletedestinationqueueresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
