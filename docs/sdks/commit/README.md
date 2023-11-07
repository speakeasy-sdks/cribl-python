# Commit
(*.commit*)

### Available Operations

* [create](#create) - create a new commit containing the current configs the given log message describing the changes.

## create

create a new commit containing the current configs the given log message describing the changes.

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.GitCommitParams(
    message='string',
)

res = s.commit.create(req)

if res.git_commit is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.GitCommitParams](../../models/shared/gitcommitparams.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateCommitResponse](../../models/operations/createcommitresponse.md)**

