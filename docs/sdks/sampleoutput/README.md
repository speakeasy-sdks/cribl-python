# sample_output

### Available Operations

* [post](#post) - Send sample data to an output to validate configuration or test connectivity

## post

Send sample data to an output to validate configuration or test connectivity

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostSampleOutputRequest(
    output_test_request=shared.OutputTestRequest(
        events=[
            shared.CriblEvent(
                raw='officiis',
            ),
            shared.CriblEvent(
                raw='inventore',
            ),
        ],
    ),
    id='763c5208-c23e-4980-ad82-f0d45eb4a8b6',
)

res = s.sample_output.post(req)

if res.output_test_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PostSampleOutputRequest](../../models/operations/postsampleoutputrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSampleOutputResponse](../../models/operations/postsampleoutputresponse.md)**

