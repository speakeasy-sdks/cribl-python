# Commit
(*commit*)

### Available Operations

* [create](#create) - create a new commit containing the current configs the given log message describing the changes.

## create

create a new commit containing the current configs the given log message describing the changes.

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.GitCommitParams(
    effective=False,
    group='minima',
    message='repellendus',
)

res = s.commit.create(req)

if res.git_commit is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.GitCommitParams](../../models/shared/gitcommitparams.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateCommitResponse](../../models/operations/createcommitresponse.md)**

