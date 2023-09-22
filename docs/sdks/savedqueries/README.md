# SavedQueries

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
    description='dicta',
    earliest='odit',
    id='5b0960a6-6815-41a4-b2af-923c5949f83f',
    latest='amet',
    name='Angela Schaefer',
    query='molestiae',
    sample_rate=395634,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='asperiores',
        enabled=False,
        keep_last_n=955466,
        tz='nobis',
    ),
    user='perspiciatis',
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


res = s.saved_queries.delete(id='accusantium')

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


res = s.saved_queries.update(id='dicta', saved_query=shared.SavedQuery(
    description='minus',
    earliest='commodi',
    id='ecbb4e24-3cf7-489f-bafe-da53e5ae6e0a',
    latest='impedit',
    name='Mattie Gibson',
    query='nobis',
    sample_rate=620054,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='minus',
        enabled=False,
        keep_last_n=154389,
        tz='magnam',
    ),
    user='reprehenderit',
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

