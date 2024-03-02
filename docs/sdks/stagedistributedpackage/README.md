# StageDistributedPackage
(*stage_distributed_package*)

### Available Operations

* [post](#post) - Stage distributed group upgrade

## post

Stage distributed group upgrade

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.stage_distributed_package.post(group='<value>', upgrade_percentage='<value>')

if res.cribl_package is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `group`                                                        | *str*                                                          | :heavy_check_mark:                                             | Group to upgrade                                               |
| `upgrade_percentage`                                           | *Optional[str]*                                                | :heavy_minus_sign:                                             | body number percentage of nodes on the worker group to upgrade |


### Response

**[operations.PostStageDistributedPackageResponse](../../models/operations/poststagedistributedpackageresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
