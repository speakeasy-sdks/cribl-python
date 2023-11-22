# RestartCriblSettings
(*restart_cribl_settings*)

### Available Operations

* [post](#post) - Restart Cribl server

## post

Restart Cribl server

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.restart_cribl_settings.post()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostRestartCriblSettingsResponse](../../models/operations/postrestartcriblsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
