# DatasetObjects
(*dataset_objects*)

### Available Operations

* [get](#get) - Get a list of Dataset objects

## get

Get a list of Dataset objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset_objects.get()

if res.datasets is not None:
    # handle response
    pass

```


### Response

**[operations.GetDatasetObjectsResponse](../../models/operations/getdatasetobjectsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4xx-5xx          | */*              |
