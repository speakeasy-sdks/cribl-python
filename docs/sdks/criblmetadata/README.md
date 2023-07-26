# cribl_metadata

### Available Operations

* [get](#get) - Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

## get

Obtain metadata which Cribl Stream/Edge uses when acting as a Service Provider

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.cribl_metadata.get()

if res.get_cribl_metadata_200_text_xml_string is not None:
    # handle response
```


### Response

**[operations.GetCriblMetadataResponse](../../models/operations/getcriblmetadataresponse.md)**

