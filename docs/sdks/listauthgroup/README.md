# ListAuthGroup
(*list_auth_group*)

### Available Operations

* [get](#get) - List the external authentication system's groups

## get

List the external authentication system's groups

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.list_auth_group.get()

if res.crud_entity_bases is not None:
    # handle response
    pass

```


### Response

**[operations.GetListAuthGroupResponse](../../models/operations/getlistauthgroupresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
