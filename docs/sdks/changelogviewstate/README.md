# ChangelogViewState
(*changelog_view_state*)

### Available Operations

* [update](#update) - Update changelog viewed state

## update

Update changelog viewed state

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.changelog_view_state.update()

if res.changelog_stateses is not None:
    # handle response
    pass
```


### Response

**[operations.UpdateChangelogViewStateResponse](../../models/operations/updatechangelogviewstateresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
