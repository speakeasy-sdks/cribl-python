# SearchDoc
(*search_doc*)

### Available Operations

* [get](#get) - Get Search documentation

## get

Get Search documentation

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.search_doc.get()

if res.get_search_doc_200_application_json_string is not None:
    # handle response
    pass
```


### Response

**[operations.GetSearchDocResponse](../../models/operations/getsearchdocresponse.md)**

