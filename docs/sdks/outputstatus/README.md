# OutputStatus
(*output_status*)

### Available Operations

* [get](#get) - Get a list of OutputStatus objects

## get

Get a list of OutputStatus objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.output_status.get()

if res.output_statuses is not None:
    # handle response
    pass
```


### Response

**[operations.GetOutputStatusResponse](../../models/operations/getoutputstatusresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
