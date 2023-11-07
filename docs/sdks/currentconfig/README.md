# CurrentConfig
(*.current_config*)

### Available Operations

* [push](#push) - push the current configs to the remote repository.

## push

push the current configs to the remote repository.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.current_config.push()

if res.push_config is not None:
    # handle response
    pass
```


### Response

**[operations.PushCurrentConfigResponse](../../models/operations/pushcurrentconfigresponse.md)**

