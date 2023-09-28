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
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SavedQuery(
    description='consectetur',
    earliest='nesciunt',
    id='4ec1b781-b36a-4080-88d1-00efada200ef',
    latest='voluptatem',
    name='Phyllis Denesik',
    query='explicabo',
    sample_rate=108903,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='aliquid',
        enabled=False,
        keep_last_n=264649,
        tz='optio',
    ),
    user='voluptatibus',
)

res = s.saved_queries.create(req)

if res.saved_query is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_queries.delete(id='molestias')

if res.saved_query is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_queries.get()

if res.saved_queries is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_queries.update(id='officia', saved_query=shared.SavedQuery(
    description='libero',
    earliest='totam',
    id='366c723f-fda9-4e06-bee4-825c1fc0e115',
    latest='optio',
    name='Joseph Purdy',
    query='iste',
    sample_rate=117819,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='quos',
        enabled=False,
        keep_last_n=356315,
        tz='dolore',
    ),
    user='modi',
))

if res.saved_query is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Unique ID                                                        |
| `saved_query`                                                    | [Optional[shared.SavedQuery]](../../models/shared/savedquery.md) | :heavy_minus_sign:                                               | SavedQuery object to be updated                                  |


### Response

**[operations.UpdateSavedQueriesResponse](../../models/operations/updatesavedqueriesresponse.md)**

