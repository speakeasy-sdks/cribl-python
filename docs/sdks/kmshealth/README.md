# KMSHealth
(*.kms_health*)

### Available Operations

* [get](#get) - Get Cribl KMS health

## get

Get Cribl KMS health

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.kms_health.get()

if res.kms_health is not None:
    # handle response
    pass
```


### Response

**[operations.GetKMSHealthResponse](../../models/operations/getkmshealthresponse.md)**

