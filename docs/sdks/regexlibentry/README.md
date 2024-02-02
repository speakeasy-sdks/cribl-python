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
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.regex_lib_entry.delete(id='string')

if res.regex_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteRegexLibEntryResponse](../../models/operations/deleteregexlibentryresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## post

Create RegexLibEntry

### Example Usage

```python
import cribl
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.RegexLibEntry(
    id='<ID>',
    regex='string',
)

res = s.regex_lib_entry.post(req)

if res.regex_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.RegexLibEntry](../../models/components/regexlibentry.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostRegexLibEntryResponse](../../models/operations/postregexlibentryresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## update

Update RegexLibEntry

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.regex_lib_entry.update(id='string', regex_lib_entry=components.RegexLibEntry(
    id='<ID>',
    regex='string',
))

if res.regex_lib_entries is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | Unique ID                                                                      |
| `regex_lib_entry`                                                              | [Optional[components.RegexLibEntry]](../../models/components/regexlibentry.md) | :heavy_minus_sign:                                                             | RegexLibEntry object to be updated                                             |


### Response

**[operations.UpdateRegexLibEntryResponse](../../models/operations/updateregexlibentryresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
