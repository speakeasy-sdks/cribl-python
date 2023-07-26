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
    description='est',
    earliest='esse',
    id='96206bef-2b0a-43e4-ac1a-a010e9aac2e9',
    latest='veritatis',
    name='Erica Hauck',
    query='fugiat',
    sample_rate=116194,
    schedule=shared.SavedQuerySchedule(
        cron_schedule='quas',
        enabled=False,
        keep_last_n=963094,
        tz='sint',
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

req = operations.DeleteSavedQueriesRequest(
    id='97a4bfad-2bf7-4d67-8a84-ad99b41d6124',
)

res = s.saved_queries.delete(req)

if res.saved_query is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteSavedQueriesRequest](../../models/operations/deletesavedqueriesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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

req = operations.UpdateSavedQueriesRequest(
    saved_query=shared.SavedQuery(
        description='velit',
        earliest='quis',
        id='31870cf6-8b03-4ad4-a1bd-43d1f0cb0a00',
        latest='perferendis',
        name='Sonja Purdy',
        query='fugiat',
        sample_rate=576751,
        schedule=shared.SavedQuerySchedule(
            cron_schedule='tempore',
            enabled=False,
            keep_last_n=213156,
            tz='dolorum',
        ),
        user='in',
    ),
    id='0d94faa7-41c5-47d1-bedc-2050d38dc3ce',
)

res = s.saved_queries.update(req)

if res.saved_query is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateSavedQueriesRequest](../../models/operations/updatesavedqueriesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateSavedQueriesResponse](../../models/operations/updatesavedqueriesresponse.md)**

