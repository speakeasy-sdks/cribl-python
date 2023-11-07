# Licenses
(*.licenses*)

### Available Operations

* [get](#get) - Get a list of License objects

## get

Get a list of License objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.licenses.get()

if res.licenses is not None:
    # handle response
    pass
```


### Response

**[operations.GetLicensesResponse](../../models/operations/getlicensesresponse.md)**

