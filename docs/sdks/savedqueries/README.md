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
    description='Multi-tiered human-resource model',
    earliest='Money blue shred',
    id='<ID>',
    latest='technology East',
    name='evolve',
    query='fuchsia Gasoline Screen',
    sample_rate=491570,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='National Durham after',
        enabled=False,
        keep_last_n=519028,
        tz='Bike',
    ),
    user='Micah.Bergnaum89',
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


res = s.saved_queries.delete(id='program')

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


res = s.saved_queries.update(id='Van', saved_query=shared.SavedQuery(
    description='Advanced encompassing orchestration',
    earliest='Metal cheater Islands',
    id='<ID>',
    latest='withdrawal extend',
    name='bifurcated',
    query='silver immediately',
    sample_rate=302461,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='JBOD',
        enabled=False,
        keep_last_n=771203,
        tz='Representative Home',
    ),
    user='Eulah_Roob',
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

