# RegexLibEntryObject
(*regex_lib_entry_object*)

### Available Operations

* [get](#get) - Get a list of RegexLibEntry objects

## get

Get a list of RegexLibEntry objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.regex_lib_entry_object.get()

if res.regex_lib_entries is not None:
    # handle response
```


### Response

**[operations.GetRegexLibEntryObjectResponse](../../models/operations/getregexlibentryobjectresponse.md)**

