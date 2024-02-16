# Groups
(*groups*)

### Available Operations

* [get](#get) - Get a list of ConfigGroup objects

## get

Get a list of ConfigGroup objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.groups.get(fields='<value>', product='<value>')

if res.config_groups is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `fields`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | additional fields to add to results: git.commit, git.localChanges, git.log |
| `product`                                                                  | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | filter to specific product: "stream" or "edge"                             |


### Response

**[operations.GetGroupsResponse](../../models/operations/getgroupsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
