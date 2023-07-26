# group_bundle

### Available Operations

* [get](#get) - Get effective bundle version for given Group

## get

Get effective bundle version for given Group

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetGroupBundleRequest(
    deploy_request=shared.DeployRequest(
        version='eum',
    ),
    id='6a6d2d00-0355-4338-8ec0-86fa21e9152c',
)

res = s.group_bundle.get(req)

if res.group_bundle is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetGroupBundleRequest](../../models/operations/getgroupbundlerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetGroupBundleResponse](../../models/operations/getgroupbundleresponse.md)**

