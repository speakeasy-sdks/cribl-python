# EventBreakerOnData

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
        condition='porro',
        delimiter='quod',
        delimiter_regex='labore',
        disabled=False,
        escape_char='ab',
        event_breaker_regex='adipisci',
        fields_=[
            shared.EventBreakerRuleFields(
                name='Orlando Homenick',
                value='est',
            ),
        ],
        fields_line_regex='recusandae',
        header_line_regex='totam',
        json_array_field='fugiat',
        json_extract_all=False,
        json_time_field='vel',
        max_event_bytes=497678,
        name='Cecil Grant',
        null_field_val='cum',
        parser='commodi',
        parser_enabled=False,
        quote_char='in',
        time_field='corporis',
        timestamp=shared.EventBreakerRuleTimestamp(
            format='reiciendis',
            length=828657,
            type=shared.EventBreakerRuleTimestampType.FORMAT,
        ),
        timestamp_anchor_regex='recusandae',
        timestamp_earliest='aliquid',
        timestamp_latest='aperiam',
        timestamp_timezone='cum',
        type=shared.EventBreakerRuleType.JSON,
    ),
    input='in',
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

