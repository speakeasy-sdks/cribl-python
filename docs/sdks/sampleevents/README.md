# SampleEvents
(*sample_events*)

### Available Operations

* [post](#post) - Sends sample events through a pipeline and returns the results

## post

Sends sample events through a pipeline and returns the results

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.PreviewDataParams(
    mode=components.Mode.ROUTE,
    pipeline_id='<value>',
    sample_id='<value>',
)

res = s.sample_events.post(req)

if res.live_data is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.PreviewDataParams](../../models/components/previewdataparams.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.PostSampleEventsResponse](../../models/operations/postsampleeventsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
