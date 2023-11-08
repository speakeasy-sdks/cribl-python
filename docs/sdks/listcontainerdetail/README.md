# ListContainerDetail
(*.list_container_detail*)

### Available Operations

* [get](#get) - Get a detailed list of containers running on the edge host.

## get

Get a detailed list of containers running on the edge host.

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.list_container_detail.get()

if res.containers is not None:
    # handle response
    pass
```


### Response

**[operations.GetListContainerDetailResponse](../../models/operations/getlistcontainerdetailresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
