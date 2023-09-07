# regex_lib_entry

### Available Operations

* [delete](#delete) - Delete RegexLibEntry
* [post](#post) - Create RegexLibEntry
* [update](#update) - Update RegexLibEntry

## delete

Delete RegexLibEntry

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.regex_lib_entry.delete(id='eaque')

if res.regex_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteRegexLibEntryResponse](../../models/operations/deleteregexlibentryresponse.md)**


## post

Create RegexLibEntry

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.RegexLibEntry(
    description='saepe',
    id='fada200e-f042-42eb-a164-cf9ab8366c72',
    lib='velit',
    regex='reiciendis',
    sample_data='repellat',
    tags='nulla',
)

res = s.regex_lib_entry.post(req)

if res.regex_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RegexLibEntry](../../models/shared/regexlibentry.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostRegexLibEntryResponse](../../models/operations/postregexlibentryresponse.md)**


## update

Update RegexLibEntry

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.regex_lib_entry.update(id='laborum', regex_lib_entry=shared.RegexLibEntry(
    description='natus',
    id='e06bee48-25c1-4fc0-a115-c80bff918544',
    lib='itaque',
    regex='maxime',
    sample_data='modi',
    tags='consequuntur',
))

if res.regex_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique ID                                                              |
| `regex_lib_entry`                                                      | [Optional[shared.RegexLibEntry]](../../models/shared/regexlibentry.md) | :heavy_minus_sign:                                                     | RegexLibEntry object to be updated                                     |


### Response

**[operations.UpdateRegexLibEntryResponse](../../models/operations/updateregexlibentryresponse.md)**

