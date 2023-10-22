# SampleOutput
(*sample_output*)

### Available Operations

* [post](#post) - Send sample data to an output to validate configuration or test connectivity

## post

Send sample data to an output to validate configuration or test connectivity

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.sample_output.post(id='string', output_test_request=shared.OutputTestRequest(
    events=[
        shared.CriblEvent(
            raw='string',
        ),
    ],
))

if res.output_test_responses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | Output Id                                                                      |
| `output_test_request`                                                          | [Optional[shared.OutputTestRequest]](../../models/shared/outputtestrequest.md) | :heavy_minus_sign:                                                             | OutputTestRequest object                                                       |


### Response

**[operations.PostSampleOutputResponse](../../models/operations/postsampleoutputresponse.md)**

