# GiveCriblVersion
(*give_cribl_version*)

### Available Operations

* [post](#post) - Upgrade Cribl to a given version

## post

Upgrade Cribl to a given version

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.give_cribl_version.post(version='payment')

if res.cribl is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `version`          | *str*              | :heavy_check_mark: | Version number     |


### Response

**[operations.PostGiveCriblVersionResponse](../../models/operations/postgivecriblversionresponse.md)**

