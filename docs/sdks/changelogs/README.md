# Changelogs
(*changelogs*)

### Available Operations

* [get](#get) - Get changelog viewed state

## get

Get changelog viewed state

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.changelogs.get()

if res.changelog_states is not None:
    # handle response
    pass
```


### Response

**[operations.GetChangelogsResponse](../../models/operations/getchangelogsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
