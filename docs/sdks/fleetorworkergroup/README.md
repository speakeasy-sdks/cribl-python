# FleetOrWorkerGroup
(*fleet_or_worker_group*)

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


res = s.fleet_or_worker_group.deploy(id='peasant', deploy_request=shared.DeployRequest(
    version='Gasoline',
))

if res.config_group is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique ID                                                              |
| `deploy_request`                                                       | [Optional[shared.DeployRequest]](../../models/shared/deployrequest.md) | :heavy_minus_sign:                                                     | DeployRequest object                                                   |


### Response

**[operations.DeployFleetOrWorkerGroupResponse](../../models/operations/deployfleetorworkergroupresponse.md)**

