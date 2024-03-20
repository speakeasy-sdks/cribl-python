# GitSettings
(*git_settings*)

### Available Operations

* [get](#get) - Get git settings
* [update](#update) - Update git settings

## get

Get git settings

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.git_settings.get()

if res.git_settings_response is not None:
    # handle response
    pass

```


### Response

**[operations.GetGitSettingsResponse](../../models/operations/getgitsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update git settings

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.git_settings.update()

if res.git_settings is not None:
    # handle response
    pass

```


### Response

**[operations.UpdateGitSettingsResponse](../../models/operations/updategitsettingsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
