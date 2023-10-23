# Bytes
(*bytes*)

### Available Operations

* [get](#get) - Get some number of bytes from the file at the given path

## get

Get some number of bytes from the file at the given path

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.bytes.get(path='string', bytes_requested=700347)

if res.sample_files is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `path`                                                                             | *str*                                                                              | :heavy_check_mark:                                                                 | The path to the file to sample                                                     |
| `bytes_requested`                                                                  | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | The number of bytes to return;   this value could be constrained by system limits. |


### Response

**[operations.GetBytesResponse](../../models/operations/getbytesresponse.md)**

