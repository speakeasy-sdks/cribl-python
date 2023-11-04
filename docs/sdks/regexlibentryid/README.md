# RegexLibEntryID
(*regex_lib_entry_id*)

### Available Operations

* [get](#get) - Get RegexLibEntry by ID

## get

Get RegexLibEntry by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.regex_lib_entry_id.get(id='string')

if res.regex_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetRegexLibEntryIDResponse](../../models/operations/getregexlibentryidresponse.md)**

