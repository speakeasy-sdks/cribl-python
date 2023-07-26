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

req = operations.DeleteRegexLibEntryRequest(
    id='c5a1f9c2-42c7-4b66-a1f3-0c73df5b6719',
)

res = s.regex_lib_entry.delete(req)

if res.regex_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteRegexLibEntryRequest](../../models/operations/deleteregexlibentryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


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
    description='voluptatum',
    id='90f42a4b-b438-4d85-b260-591d745e3c20',
    lib='veniam',
    regex='sint',
    sample_data='minus',
    tags='excepturi',
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

req = operations.UpdateRegexLibEntryRequest(
    regex_lib_entry=shared.RegexLibEntry(
        description='porro',
        id='3f567e0e-2527-465b-9d62-fcdace1f0121',
        lib='laboriosam',
        regex='quod',
        sample_data='repudiandae',
        tags='consequuntur',
    ),
    id='239e8f25-cd0d-419d-959f-439e39266cbd',
)

res = s.regex_lib_entry.update(req)

if res.regex_lib_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateRegexLibEntryRequest](../../models/operations/updateregexlibentryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.UpdateRegexLibEntryResponse](../../models/operations/updateregexlibentryresponse.md)**

