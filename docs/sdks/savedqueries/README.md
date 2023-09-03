# saved_queries

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
    description='ab',
    earliest='magnam',
    id='db6be5a6-8599-48e2-aae2-0da16fc2b271',
    latest='deserunt',
    name='Vickie Marvin',
    query='molestiae',
    sample_rate=933840,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='rem',
        enabled=False,
        keep_last_n=366327,
        tz='non',
    ),
    user='recusandae',
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


res = s.saved_queries.delete(id='omnis')

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


res = s.saved_queries.update(id='ipsa', saved_query=shared.SavedQuery(
    description='aliquam',
    earliest='dolor',
    id='9d222465-6946-4240-b084-f7ab37cef022',
    latest='consequuntur',
    name='Jean Mayert',
    query='quidem',
    sample_rate=350202,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='veniam',
        enabled=False,
        keep_last_n=267988,
        tz='quasi',
    ),
    user='quae',
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

