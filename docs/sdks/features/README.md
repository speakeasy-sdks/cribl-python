# Features
(*features*)

### Available Operations

* [get](#get) - List all features

## get

List all features

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.features.get()

if res.features_entries is not None:
    # handle response
    pass

```


### Response

**[operations.GetFeaturesResponse](../../models/operations/getfeaturesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
