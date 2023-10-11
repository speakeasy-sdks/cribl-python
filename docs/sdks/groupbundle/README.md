# GroupBundle
(*group_bundle*)

### Available Operations

* [get](#get) - Get effective bundle version for given Group

## get

Get effective bundle version for given Group

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.group_bundle.get(id='female', deploy_request=shared.DeployRequest(
    version='Hatchback Kia',
))

if res.group_bundle is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Group ID                                                               |
| `deploy_request`                                                       | [Optional[shared.DeployRequest]](../../models/shared/deployrequest.md) | :heavy_minus_sign:                                                     | DeployRequest object                                                   |


### Response

**[operations.GetGroupBundleResponse](../../models/operations/getgroupbundleresponse.md)**

