# grok_file

### Available Operations

* [create](#create) - Create GrokFile
* [delete](#delete) - Delete GrokFile
* [get](#get) - Get GrokFile by ID
* [update](#update) - Update GrokFile

## create

Create GrokFile

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.GrokFile(
    content='possimus',
    id='20e56248-fff6-439a-910a-bdcab6267669',
    size=385760,
    tags='accusamus',
)

res = s.grok_file.create(req)

if res.grok_file is not None:
    # handle response
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [shared.GrokFile](../../models/shared/grokfile.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.CreateGrokFileResponse](../../models/operations/creategrokfileresponse.md)**


## delete

Delete GrokFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteGrokFileRequest(
    id='1ec00221-b335-4d89-acb3-ecfda8d0c549',
)

res = s.grok_file.delete(req)

if res.grok_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteGrokFileRequest](../../models/operations/deletegrokfilerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteGrokFileResponse](../../models/operations/deletegrokfileresponse.md)**


## get

Get GrokFile by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetGrokFileRequest(
    id='ef030049-78a6-41fa-9cf2-0688f77c1ffc',
)

res = s.grok_file.get(req)

if res.grok_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetGrokFileRequest](../../models/operations/getgrokfilerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetGrokFileResponse](../../models/operations/getgrokfileresponse.md)**


## update

Update GrokFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateGrokFileRequest(
    grok_file=shared.GrokFile(
        content='voluptate',
        id='1dca163f-2a3c-480a-97ff-334cddf857a9',
        size=915647,
        tags='eum',
    ),
    id='1876c6ab-21d2-49df-894d-6fecd7993900',
)

res = s.grok_file.update(req)

if res.grok_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateGrokFileRequest](../../models/operations/updategrokfilerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateGrokFileResponse](../../models/operations/updategrokfileresponse.md)**

