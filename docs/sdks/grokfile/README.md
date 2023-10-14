# GrokFile
(*grok_file*)

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
    bearer_auth="",
)

req = shared.GrokFile(
    content='bluetooth Extended',
    id='<ID>',
    size=134365,
)

res = s.grok_file.create(req)

if res.grok_file is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.grok_file.delete(id='program')

if res.grok_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteGrokFileResponse](../../models/operations/deletegrokfileresponse.md)**


## get

Get GrokFile by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.grok_file.get(id='female')

if res.grok_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetGrokFileResponse](../../models/operations/getgrokfileresponse.md)**


## update

Update GrokFile

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.grok_file.update(id='Van', grok_file=shared.GrokFile(
    content='Reactive',
    id='<ID>',
    size=991464,
))

if res.grok_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique ID                                                    |
| `grok_file`                                                  | [Optional[shared.GrokFile]](../../models/shared/grokfile.md) | :heavy_minus_sign:                                           | GrokFile object to be updated                                |


### Response

**[operations.UpdateGrokFileResponse](../../models/operations/updategrokfileresponse.md)**

