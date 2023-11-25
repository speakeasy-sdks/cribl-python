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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="",
)

req = components.GrokFile(
    content='string',
    id='<ID>',
    size=486589,
)

res = s.grok_file.create(req)

if res.grok_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [components.GrokFile](../../models/components/grokfile.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateGrokFileResponse](../../models/operations/creategrokfileresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## delete

Delete GrokFile

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.grok_file.delete(id='string')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get GrokFile by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.grok_file.get(id='string')

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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update GrokFile

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="",
)


res = s.grok_file.update(id='string', grok_file=components.GrokFile(
    content='string',
    id='<ID>',
    size=857478,
))

if res.grok_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique ID                                                            |
| `grok_file`                                                          | [Optional[components.GrokFile]](../../models/components/grokfile.md) | :heavy_minus_sign:                                                   | GrokFile object to be updated                                        |


### Response

**[operations.UpdateGrokFileResponse](../../models/operations/updategrokfileresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
