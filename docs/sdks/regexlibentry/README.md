# RegexLibEntry
(*regex_lib_entry*)

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


res = s.regex_lib_entry.delete(id='animi')

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
    description='dolores',
    id='b12eb07f-116d-4b99-945f-c95fa88970e1',
    lib='quos',
    regex='iste',
    sample_data='assumenda',
    tags='tempore',
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


res = s.regex_lib_entry.update(id='libero', regex_lib_entry=shared.RegexLibEntry(
    description='velit',
    id='0fcb33ea-055b-4197-8d44-e2f52d82d351',
    lib='velit',
    regex='facilis',
    sample_data='tempore',
    tags='nisi',
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

