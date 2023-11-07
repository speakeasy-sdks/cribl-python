# OutputStatus
(*.output_status*)

### Available Operations

* [get](#get) - Get a list of OutputStatus objects

## get

Get a list of OutputStatus objects

### Example Usage

```python
import cribl

s = cribl.Cribl(
    bearer_auth="",
)


res = s.output_status.get()

if res.output_statuses is not None:
    # handle response
    pass
```


### Response

**[operations.GetOutputStatusResponse](../../models/operations/getoutputstatusresponse.md)**

