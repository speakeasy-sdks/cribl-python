# KMSConfig
(*kms_config*)

### Available Operations

* [get](#get) - Get Cribl KMS config
* [update](#update) - Update Cribl KMS config

## get

Get Cribl KMS config

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.kms_config.get()

if res.kms_configs is not None:
    # handle response
    pass
```


### Response

**[operations.GetKMSConfigResponse](../../models/operations/getkmsconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update Cribl KMS config

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.IKMSProviderConfig(
    enable_health_check=False,
    engine=components.VaultKMSEngineConfig(
        type=components.VaultKMSEngineConfigType.KV2,
    ),
    provider=components.SecretProvider.AWS_KMS,
    service=components.IAWSKMSServiceConfig(
        kms_key_arn='string',
        region='string',
    ),
)

res = s.kms_config.update(req)

if res.ikms_provider_config is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.IKMSProviderConfig](../../models/components/ikmsproviderconfig.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpdateKMSConfigResponse](../../models/operations/updatekmsconfigresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
