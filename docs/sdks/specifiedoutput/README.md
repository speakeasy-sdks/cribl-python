# SpecifiedOutput
(*specified_output*)

### Available Operations

* [get](#get) - Get samples data for the specified output. Used to get sample data for the test action.

## get

Get samples data for the specified output. Used to get sample data for the test action.

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.specified_output.get(id='female')

if res.get_specified_output_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Output Id          |


### Response

**[operations.GetSpecifiedOutputResponse](../../models/operations/getspecifiedoutputresponse.md)**

