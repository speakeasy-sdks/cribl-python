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
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.SavedQuery(
    id='<ID>',
    name='string',
    query='string',
    schedule=shared.SavedQuerySchedule(
        cron_schedule='string',
        enabled=False,
        keep_last_n=486589,
        tz='string',
    ),
)

res = s.saved_queries.create(req)

if res.saved_query is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.SavedQuery](../../models/shared/savedquery.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateSavedQueriesResponse](../../models/operations/createsavedqueriesresponse.md)**


## delete

Delete SavedQuery

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
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


## get

Get a list of SavedQuery objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_queries.get()

if res.saved_queries is not None:
    # handle response
    pass
```


### Response

**[operations.GetSavedQueriesResponse](../../models/operations/getsavedqueriesresponse.md)**


## update

Update SavedQuery

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.saved_queries.update(id='string', saved_query=shared.SavedQuery(
    id='<ID>',
    name='string',
    query='string',
    schedule=shared.SavedQuerySchedule(
        cron_schedule='string',
        enabled=False,
        keep_last_n=857478,
        tz='string',
    ),
))

if res.saved_query is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Unique ID                                                        |
| `saved_query`                                                    | [Optional[shared.SavedQuery]](../../models/shared/savedquery.md) | :heavy_minus_sign:                                               | SavedQuery object to be updated                                  |


### Response

**[operations.UpdateSavedQueriesResponse](../../models/operations/updatesavedqueriesresponse.md)**

