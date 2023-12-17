# Certificates
(*certificates*)

### Available Operations

* [get](#get) - Get a list of Certificate objects

## get

Get a list of Certificate objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.certificates.get()

if res.certificates is not None:
    # handle response
    pass
```


### Response

**[operations.GetCertificatesResponse](../../models/operations/getcertificatesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
