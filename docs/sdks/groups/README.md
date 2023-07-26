# groups

### Available Operations

* [get](#get) - Get a list of ConfigGroup objects

## get

Get a list of ConfigGroup objects

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetGroupsRequest(
    fields_='quidem',
    product='non',
)

res = s.groups.get(req)

if res.config_groups is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetGroupsRequest](../../models/operations/getgroupsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetGroupsResponse](../../models/operations/getgroupsresponse.md)**

