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
        clean_fields=False,
        condition='Producer base',
        delimiter='protocol off beside',
        delimiter_regex='Arizona synthesizing',
        disabled=False,
        escape_char='content intelligence array',
        event_breaker_regex='Clothing array Kids',
        fields_=[
            shared.EventBreakerRuleFields(
                name='Integration HTTP',
                value='Hybrid open compress',
            ),
        ],
        fields_line_regex='Dollar',
        header_line_regex='Southeast deposit Bicycle',
        json_array_field='dynamic',
        json_extract_all=False,
        json_time_field='Folk hm',
        max_event_bytes=759000,
        name='gullible nose',
        null_field_val='Mouse Clemente',
        parser='XML',
        parser_enabled=False,
        quote_char='Soap bah deploy',
        time_field='primary',
        timestamp=shared.EventBreakerRuleTimestamp(
            format='Research Egypt',
            length=181401,
            type=shared.EventBreakerRuleTimestampType.CURRENT,
        ),
        timestamp_anchor_regex='Reggae Hybrid',
        timestamp_earliest='array',
        timestamp_latest='rich Investor',
        timestamp_timezone='weird revolutionize',
        type=shared.EventBreakerRuleType.HEADER,
    ),
    input='degree',
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

