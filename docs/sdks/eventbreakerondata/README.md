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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DatatypePreviewRequestBody(
    event_breaker_rule=shared.EventBreakerRule(
        condition='Producer base',
        fields_=[
            shared.EventBreakerRuleFields(
                name='protocol off beside',
                value='Arizona synthesizing',
            ),
        ],
        max_event_bytes=767148,
        name='withdrawal',
        timestamp=shared.EventBreakerRuleTimestamp(
            type=shared.EventBreakerRuleTimestampType.AUTO,
        ),
        timestamp_anchor_regex='Southeast array',
        timestamp_timezone='Clothing array Kids',
    ),
    input='Classical',
)

res = s.event_breaker_on_data.post(req)

if res.preview_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.DatatypePreviewRequestBody](../../models/shared/datatypepreviewrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PostEventBreakerOnDataResponse](../../models/operations/posteventbreakerondataresponse.md)**

