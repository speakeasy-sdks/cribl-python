# SearchLimits
(*search_limits*)

### Available Operations

* [get](#get) - Get search limits

## get

Get search limits

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_limits.get()

if res.search_settingses is not None:
    # handle response
    pass
```


### Response

**[operations.GetSearchLimitsResponse](../../models/operations/getsearchlimitsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
