# ChangedFiles
(*changed_files*)

### Available Operations

* [get](#get) - get the files changed

## get

get the files changed

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.changed_files.get(id='female', group='program')

if res.changed_files is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *Optional[str]*    | :heavy_minus_sign: | Commit ID          |
| `group`            | *Optional[str]*    | :heavy_minus_sign: | Group ID           |


### Response

**[operations.GetChangedFilesResponse](../../models/operations/getchangedfilesresponse.md)**

