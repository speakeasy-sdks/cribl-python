# RegexLibEntry

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


res = s.regex_lib_entry.delete(id='illo')

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
    description='hic',
    id='af4b7544-e472-4e80-a857-a5b40463a7d5',
    lib='molestiae',
    regex='veniam',
    sample_data='reiciendis',
    tags='ab',
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


res = s.regex_lib_entry.update(id='modi', regex_lib_entry=shared.RegexLibEntry(
    description='aut',
    id='0e764ad7-334e-4c1b-b81b-36a08088d100',
    lib='saepe',
    regex='delectus',
    sample_data='mollitia',
    tags='nulla',
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

