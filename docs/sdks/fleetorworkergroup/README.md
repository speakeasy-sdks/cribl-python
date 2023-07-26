# fleet_or_worker_group

### Available Operations

* [deploy](#deploy) - Deploy commits for a Fleet or Worker Group

## deploy

Deploy commits for a Fleet or Worker Group

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeployFleetOrWorkerGroupRequest(
    deploy_request=shared.DeployRequest(
        version='est',
    ),
    id='4fa87cf5-35a6-4fae-94eb-f60c321f023b',
)

res = s.fleet_or_worker_group.deploy(req)

if res.config_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.DeployFleetOrWorkerGroupRequest](../../models/operations/deployfleetorworkergrouprequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.DeployFleetOrWorkerGroupResponse](../../models/operations/deployfleetorworkergroupresponse.md)**

