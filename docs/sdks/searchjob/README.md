# SearchJob
(*search_job*)

### Available Operations

* [create](#create) - Create SearchJob
* [delete](#delete) - Delete SearchJob
* [get](#get) - Get SearchJob by ID
* [update](#update) - Update SearchJob

## create

Create SearchJob

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.SearchJob(
    group='<value>',
    id='<id>',
    query='<value>',
    search_config=components.SearchConfig(
        datasets=[
            '<value>',
        ],
        has_send_operator=False,
        ordered_field_names=[
            '<value>',
        ],
        search_terms=[
            components.SearchTerm(
                is_case_sensitive=False,
                term='<value>',
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    status=components.SearchJobStatus.COMPLETED,
    time_created=489382,
    user='Loyal.Stokes',
)

res = s.search_job.create(req)

if res.search_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.SearchJob](../../models/components/searchjob.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateSearchJobResponse](../../models/operations/createsearchjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## delete

Delete SearchJob

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_job.delete(id='<value>')

if res.search_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteSearchJobResponse](../../models/operations/deletesearchjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## get

Get SearchJob by ID

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_job.get(id='<value>')

if res.search_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetSearchJobResponse](../../models/operations/getsearchjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update SearchJob

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.search_job.update(id='<value>', search_job=components.SearchJob(
    group='<value>',
    id='<id>',
    query='<value>',
    search_config=components.SearchConfig(
        datasets=[
            '<value>',
        ],
        has_send_operator=False,
        ordered_field_names=[
            '<value>',
        ],
        search_terms=[
            components.SearchTerm(
                is_case_sensitive=False,
                term='<value>',
            ),
        ],
        suppress_event_marking=False,
        use_formatted_visualization=False,
    ),
    status=components.SearchJobStatus.QUEUED,
    time_created=24555,
    user='Lavern_Armstrong',
))

if res.search_job is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique ID                                                              |
| `search_job`                                                           | [Optional[components.SearchJob]](../../models/components/searchjob.md) | :heavy_minus_sign:                                                     | SearchJob object to be updated                                         |


### Response

**[operations.UpdateSearchJobResponse](../../models/operations/updatesearchjobresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
