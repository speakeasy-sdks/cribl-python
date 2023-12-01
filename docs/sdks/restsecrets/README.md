# RestSecrets
(*rest_secrets*)

### Available Operations

* [get](#get) - Get a list of RestSecret objects

## get

Get a list of RestSecret objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.rest_secrets.get()

if res.rest_secrets is not None:
    # handle response
    pass
```


### Response

**[operations.GetRestSecretsResponse](../../models/operations/getrestsecretsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
