# GiveCriblVersion
(*give_cribl_version*)

### Available Operations

* [post](#post) - Upgrade Cribl to a given version

## post

Upgrade Cribl to a given version

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.give_cribl_version.post(version='<value>')

if res.cribl is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `version`          | *str*              | :heavy_check_mark: | Version number     |


### Response

**[operations.PostGiveCriblVersionResponse](../../models/operations/postgivecriblversionresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
