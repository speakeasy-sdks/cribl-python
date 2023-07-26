# regex_lib_entry_id

### Available Operations

* [get](#get) - Get RegexLibEntry by ID

## get

Get RegexLibEntry by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetRegexLibEntryIDRequest(
    id='95f7aa2b-2411-4369-9d1e-6698fcc45962',
)

res = s.regex_lib_entry_id.get(req)

if res.regex_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetRegexLibEntryIDRequest](../../models/operations/getregexlibentryidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetRegexLibEntryIDResponse](../../models/operations/getregexlibentryidresponse.md)**

