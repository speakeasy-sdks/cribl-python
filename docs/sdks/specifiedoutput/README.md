# specified_output

### Available Operations

* [get](#get) - Get samples data for the specified output. Used to get sample data for the test action.

## get

Get samples data for the specified output. Used to get sample data for the test action.

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSpecifiedOutputRequest(
    id='4b171068-8dee-4bef-897f-3dd0ccd33f11',
)

res = s.specified_output.get(req)

if res.get_specified_output_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetSpecifiedOutputRequest](../../models/operations/getspecifiedoutputrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetSpecifiedOutputResponse](../../models/operations/getspecifiedoutputresponse.md)**

