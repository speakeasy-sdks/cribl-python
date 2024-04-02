# GroupBundle
(*group_bundle*)

### Available Operations

* [get](#get) - Get effective bundle version for given Group

## get

Get effective bundle version for given Group

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.group_bundle.get(id='<value>', deploy_request=components.DeployRequest(
    version='<value>',
))

if res.group_bundle is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | Group ID                                                                       |
| `deploy_request`                                                               | [Optional[components.DeployRequest]](../../models/components/deployrequest.md) | :heavy_minus_sign:                                                             | DeployRequest object                                                           |


### Response

**[operations.GetGroupBundleResponse](../../models/operations/getgroupbundleresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
