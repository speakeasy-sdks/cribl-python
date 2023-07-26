# kms_config

### Available Operations

* [get](#get) - Get Cribl KMS config
* [update](#update) - Update Cribl KMS config

## get

Get Cribl KMS config

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.kms_config.get()

if res.kms_configs is not None:
    # handle response
```


### Response

**[operations.GetKMSConfigResponse](../../models/operations/getkmsconfigresponse.md)**


## update

Update Cribl KMS config

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.IKMSProviderConfig(
    enable_health_check=False,
    engine=shared.VaultKMSEngineConfig(
        mount='ullam',
        secret_path='numquam',
        type=shared.VaultKMSEngineConfigType.KV2,
    ),
    health_check_endpoint='enim',
    namespace='cupiditate',
    provider=shared.SecretProvider.VAULT,
    secret_dir='itaque',
    service=shared.IAWSKMSServiceConfig(
        kms_key_arn='fuga',
        region='consectetur',
    ),
    url='modi',
)

res = s.kms_config.update(req)

if res.ikms_provider_config is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.IKMSProviderConfig](../../models/shared/ikmsproviderconfig.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.UpdateKMSConfigResponse](../../models/operations/updatekmsconfigresponse.md)**

