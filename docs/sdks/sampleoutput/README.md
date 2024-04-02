# SampleOutput
(*sample_output*)

### Available Operations

* [post](#post) - Send sample data to an output to validate configuration or test connectivity

## post

Send sample data to an output to validate configuration or test connectivity

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sample_output.post(id='<value>', output_test_request=components.OutputTestRequest(
    events=[
        components.CriblEvent(
            raw='<value>',
        ),
    ],
))

if res.output_test_responses is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | Output Id                                                                              |
| `output_test_request`                                                                  | [Optional[components.OutputTestRequest]](../../models/components/outputtestrequest.md) | :heavy_minus_sign:                                                                     | OutputTestRequest object                                                               |


### Response

**[operations.PostSampleOutputResponse](../../models/operations/postsampleoutputresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
