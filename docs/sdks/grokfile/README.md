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
    content='nihil',
    id='411faf4b-7544-4e47-ae80-2857a5b40463',
    size=652125,
    tags='dignissimos',
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


res = s.grok_file.delete(id='fugiat')

if res.grok_file is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.grok_file.get(id='nostrum')

if res.grok_file is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.grok_file.update(id='molestiae', grok_file=shared.GrokFile(
    content='veniam',
    id='f1400e76-4ad7-4334-ac1b-781b36a08088',
    size=832239,
    tags='veritatis',
))

if res.grok_file is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | Unique ID                                                    |
| `grok_file`                                                  | [Optional[shared.GrokFile]](../../models/shared/grokfile.md) | :heavy_minus_sign:                                           | GrokFile object to be updated                                |


### Response

**[operations.UpdateGrokFileResponse](../../models/operations/updategrokfileresponse.md)**

