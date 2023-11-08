# SearchJobs
(*.search_jobs*)

### Available Operations

* [get](#get) - Get a list of SearchJob objects

## get

Get a list of SearchJob objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.search_jobs.get()

if res.search_jobs is not None:
    # handle response
    pass
```


### Response

**[operations.GetSearchJobsResponse](../../models/operations/getsearchjobsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
