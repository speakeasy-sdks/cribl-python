# RouteLists
(*route_lists*)

### Available Operations

* [get](#get) - List all routes

## get

List all routes

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.route_lists.get()

if res.routes is not None:
    # handle response
    pass
```


### Response

**[operations.GetRouteListsResponse](../../models/operations/getroutelistsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
