<!-- Start SDK Example Usage [usage] -->
```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->