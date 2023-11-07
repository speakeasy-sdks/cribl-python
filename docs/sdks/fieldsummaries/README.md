# FieldSummaries
(*.field_summaries*)

### Available Operations

* [get](#get) - List field summaries

## get

List field summaries

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.field_summaries.get(id='string')

if res.field_summaries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | search job id      |


### Response

**[operations.GetFieldSummariesResponse](../../models/operations/getfieldsummariesresponse.md)**

