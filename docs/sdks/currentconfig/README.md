# CurrentConfig
(*current_config*)

### Available Operations

* [push](#push) - push the current configs to the remote repository.

## push

push the current configs to the remote repository.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.current_config.push()

if res.push_config is not None:
    # handle response
    pass

```


### Response

**[operations.PushCurrentConfigResponse](../../models/operations/pushcurrentconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
