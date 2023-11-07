# FleetOrWorkerGroup
(*.fleet_or_worker_group*)

### Available Operations

* [deploy](#deploy) - Deploy commits for a Fleet or Worker Group

## deploy

Deploy commits for a Fleet or Worker Group

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.fleet_or_worker_group.deploy(id='string', deploy_request=components.DeployRequest(
    version='string',
))

if res.config_group is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | Unique ID                                                                  |
| `deploy_request`                                                           | [Optional[components.DeployRequest]](../../models/shared/deployrequest.md) | :heavy_minus_sign:                                                         | DeployRequest object                                                       |


### Response

**[operations.DeployFleetOrWorkerGroupResponse](../../models/operations/deployfleetorworkergroupresponse.md)**

