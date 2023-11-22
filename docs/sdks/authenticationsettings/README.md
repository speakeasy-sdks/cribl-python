# AuthenticationSettings
(*authentication_settings*)

### Available Operations

* [get](#get) - Get authentication settings
* [update](#update) - Update authentication settings

## get

Get authentication settings

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.authentication_settings.get()

if res.auth_configs is not None:
    # handle response
    pass
```


### Response

**[operations.GetAuthenticationSettingsResponse](../../models/operations/getauthenticationsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update authentication settings

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.authentication_settings.update()

if res.auth_configs is not None:
    # handle response
    pass
```


### Response

**[operations.UpdateAuthenticationSettingsResponse](../../models/operations/updateauthenticationsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
