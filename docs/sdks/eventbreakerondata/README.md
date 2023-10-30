# EventBreakerOnData
(*event_breaker_on_data*)

### Available Operations

* [post](#post) - Runs an event breaker rule on the specified data

## post

Runs an event breaker rule on the specified data

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.DatatypePreviewRequestBody(
    event_breaker_rule=shared.EventBreakerRule(
        condition='string',
        fields=[
            shared.EventBreakerRuleFields(
                name='string',
                value='string',
            ),
        ],
        max_event_bytes=449035,
        name='string',
        timestamp=shared.EventBreakerRuleTimestamp(
            type=shared.EventBreakerRuleTimestampType.CURRENT,
        ),
        timestamp_anchor_regex='string',
        timestamp_timezone='string',
    ),
    input='string',
)

res = s.event_breaker_on_data.post(req)

if res.preview_responses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.DatatypePreviewRequestBody](../../models/shared/datatypepreviewrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PostEventBreakerOnDataResponse](../../models/operations/posteventbreakerondataresponse.md)**

