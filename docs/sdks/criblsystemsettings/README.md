# CriblSystemSettings
(*cribl_system_settings*)

### Available Operations

* [get](#get) - Get Cribl system settings
* [update](#update) - Update Cribl system settings

## get

Get Cribl system settings

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.cribl_system_settings.get()

if res.system_settings is not None:
    # handle response
    pass
```


### Response

**[operations.GetCriblSystemSettingsResponse](../../models/operations/getcriblsystemsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update Cribl system settings

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.cribl_system_settings.update()

if res.system_settingses is not None:
    # handle response
    pass
```


### Response

**[operations.UpdateCriblSystemSettingsResponse](../../models/operations/updatecriblsystemsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
