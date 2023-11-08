# GiveCriblVersion
(*.give_cribl_version*)

### Available Operations

* [post](#post) - Upgrade Cribl to a given version

## post

Upgrade Cribl to a given version

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.give_cribl_version.post(version='string')

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
| errors.SDKError  | 400-600          | */*              |
