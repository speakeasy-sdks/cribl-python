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
        condition='eum',
        delimiter='reprehenderit',
        delimiter_regex='voluptatum',
        disabled=False,
        escape_char='blanditiis',
        event_breaker_regex='nihil',
        fields_=[
            shared.EventBreakerRuleFields(
                name='Doug Littel',
                value='architecto',
            ),
            shared.EventBreakerRuleFields(
                name='Lloyd Ledner V',
                value='placeat',
            ),
            shared.EventBreakerRuleFields(
                name='Clara Williamson',
                value='officia',
            ),
        ],
        fields_line_regex='natus',
        header_line_regex='cumque',
        json_array_field='natus',
        json_extract_all=False,
        json_time_field='quaerat',
        max_event_bytes=985379,
        name='Gretchen O'Hara',
        null_field_val='enim',
        parser='eum',
        parser_enabled=False,
        quote_char='nemo',
        time_field='illum',
        timestamp=shared.EventBreakerRuleTimestamp(
            format='nesciunt',
            length=22331,
            type=shared.EventBreakerRuleTimestampType.FORMAT,
        ),
        timestamp_anchor_regex='minus',
        timestamp_earliest='asperiores',
        timestamp_latest='recusandae',
        timestamp_timezone='voluptates',
        type=shared.EventBreakerRuleType.HEADER,
    ),
    input='dicta',
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

