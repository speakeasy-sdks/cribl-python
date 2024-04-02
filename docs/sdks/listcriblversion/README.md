# ListCriblVersion
(*list_cribl_version*)

### Available Operations

* [get](#get) - Get a list of Cribl versions available for upgrade

## get

Get a list of Cribl versions available for upgrade

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_cribl_version.get()

if res.upgrade_results is not None:
    # handle response
    pass

```


### Response

**[operations.GetListCriblVersionResponse](../../models/operations/getlistcriblversionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
