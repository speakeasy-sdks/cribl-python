<!-- Start SDK Example Usage -->


```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.appscope_lib_entries.get()

if res.app_scope_lib_entries is not None:
    # handle response
```
<!-- End SDK Example Usage -->