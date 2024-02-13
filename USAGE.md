<!-- Start SDK Example Usage [usage] -->
```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.idp_auth.get(code='string', state='string')

if res.success is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->