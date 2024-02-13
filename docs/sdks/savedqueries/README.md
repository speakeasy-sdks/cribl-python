# SavedQueries
(*saved_queries*)

### Available Operations

* [create](#create) - Create SavedQuery
* [delete](#delete) - Delete SavedQuery
* [get](#get) - Get a list of SavedQuery objects
* [update](#update) - Update SavedQuery

## create

Create SavedQuery

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.SavedQuery(
    id='<ID>',
    name='string',
    query='string',
)

res = s.saved_queries.create(req)

if res.saved_query is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [components.SavedQuery](../../models/components/savedquery.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateSavedQueriesResponse](../../models/operations/createsavedqueriesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete SavedQuery

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saved_queries.delete(id='string')

if res.saved_query is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteSavedQueriesResponse](../../models/operations/deletesavedqueriesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get a list of SavedQuery objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saved_queries.get()

if res.saved_queries is not None:
    # handle response
    pass
```


### Response

**[operations.GetSavedQueriesResponse](../../models/operations/getsavedqueriesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update SavedQuery

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saved_queries.update(id='string', saved_query=components.SavedQuery(
    id='<ID>',
    name='string',
    query='string',
))

if res.saved_query is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | Unique ID                                                                |
| `saved_query`                                                            | [Optional[components.SavedQuery]](../../models/components/savedquery.md) | :heavy_minus_sign:                                                       | SavedQuery object to be updated                                          |


### Response

**[operations.UpdateSavedQueriesResponse](../../models/operations/updatesavedqueriesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
