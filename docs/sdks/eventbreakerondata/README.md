# event_breaker_on_data

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
        condition='doloremque',
        delimiter='quis',
        delimiter_regex='veniam',
        disabled=False,
        escape_char='libero',
        event_breaker_regex='architecto',
        fields_=[
            shared.EventBreakerRuleFields(
                name='Sheri Schuppe',
                value='itaque',
            ),
            shared.EventBreakerRuleFields(
                name='Ollie Harris',
                value='laudantium',
            ),
            shared.EventBreakerRuleFields(
                name='Freda Farrell I',
                value='facilis',
            ),
        ],
        fields_line_regex='tempore',
        header_line_regex='nisi',
        json_array_field='voluptatibus',
        json_extract_all=False,
        json_time_field='quaerat',
        max_event_bytes=503748,
        name='Charlie Harvey',
        null_field_val='minus',
        parser='facere',
        parser_enabled=False,
        quote_char='facilis',
        time_field='ipsum',
        timestamp=shared.EventBreakerRuleTimestamp(
            format='ad',
            length=973819,
            type=shared.EventBreakerRuleTimestampType.CURRENT,
        ),
        timestamp_anchor_regex='consequuntur',
        timestamp_earliest='debitis',
        timestamp_latest='labore',
        timestamp_timezone='rerum',
        type=shared.EventBreakerRuleType.JSON,
    ),
    input='reprehenderit',
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

