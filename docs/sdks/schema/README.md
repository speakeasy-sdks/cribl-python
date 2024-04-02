# Schema
(*schema*)

### Available Operations

* [create](#create) - Create Schema
* [delete](#delete) - Delete Schema
* [get](#get) - Get Schema by ID
* [post](#post) - Create Schema
* [update](#update) - Update Schema

## create

Create Schema

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.SchemaLibEntry(
    id='<id>',
    schema='<value>',
)

res = s.schema.create(req)

if res.schema_lib_entry is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.SchemaLibEntry](../../models/components/schemalibentry.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreateSchemaResponse](../../models/operations/createschemaresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## delete

Delete Schema

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.schema.delete(id='<value>')

if res.schema_lib_entry is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteSchemaResponse](../../models/operations/deleteschemaresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## get

Get Schema by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.schema.get(id='<value>')

if res.schema_lib_entry is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetSchemaResponse](../../models/operations/getschemaresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## post

Create Schema

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.SchemaLibEntry(
    id='<id>',
    schema='<value>',
)

res = s.schema.post(req)

if res.schema_lib_entries is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.SchemaLibEntry](../../models/components/schemalibentry.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostSchemaResponse](../../models/operations/postschemaresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |

## update

Update Schema

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.schema.update(id='<value>', schema_lib_entry=components.SchemaLibEntry(
    id='<id>',
    schema='<value>',
))

if res.schema_lib_entry is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | Unique ID                                                                        |
| `schema_lib_entry`                                                               | [Optional[components.SchemaLibEntry]](../../models/components/schemalibentry.md) | :heavy_minus_sign:                                                               | Schema object to be updated                                                      |


### Response

**[operations.UpdateSchemaResponse](../../models/operations/updateschemaresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
