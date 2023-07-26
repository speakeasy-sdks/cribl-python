# parser_id

### Available Operations

* [delete](#delete) - Delete Parser
* [get](#get) - Get Parser by ID
* [update](#update) - Update Parser

## delete

Delete Parser

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteParserIDRequest(
    id='922151fe-1712-4099-853e-9f543d854439',
)

res = s.parser_id.delete(req)

if res.parser_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteParserIDRequest](../../models/operations/deleteparseridrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteParserIDResponse](../../models/operations/deleteparseridresponse.md)**


## get

Get Parser by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetParserIDRequest(
    id='ee224460-443b-4c15-8188-c2f56e85da78',
)

res = s.parser_id.get(req)

if res.parser_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetParserIDRequest](../../models/operations/getparseridrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetParserIDResponse](../../models/operations/getparseridresponse.md)**


## update

Update Parser

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateParserIDRequest(
    request_body={
        "odit": 'officiis',
    },
    id='abd617c3-b0d5-41a4-8bf0-1bad8706d460',
)

res = s.parser_id.update(req)

if res.parser_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateParserIDRequest](../../models/operations/updateparseridrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateParserIDResponse](../../models/operations/updateparseridresponse.md)**

