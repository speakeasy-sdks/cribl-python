# Datasets
(*datasets*)

### Available Operations

* [get](#get) - Get a list of DatasetProviderType objects

## get

Get a list of DatasetProviderType objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.datasets.get()

if res.dataset_provider_types is not None:
    # handle response
    pass
```


### Response

**[operations.GetDatasetProviderTypesResponse](../../models/operations/getdatasetprovidertypesresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
