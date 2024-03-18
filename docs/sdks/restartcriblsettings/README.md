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
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.restart_cribl_settings.post()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostRestartCriblSettingsResponse](../../models/operations/postrestartcriblsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
