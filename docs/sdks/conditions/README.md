# Conditions
(*.conditions*)

### Available Operations

* [get](#get) - Get a list of Condition objects

## get

Get a list of Condition objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.conditions.get()

if res.conditions is not None:
    # handle response
    pass
```


### Response

**[operations.GetConditionsResponse](../../models/operations/getconditionsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
