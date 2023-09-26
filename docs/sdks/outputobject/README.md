# OutputObject

### Available Operations

* [create](#create) - Create Output

## create

Create Output

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.OutputStatsdExt(
    connection_timeout=491892,
    environment='optio',
    flush_period_sec=898961,
    host='corporis',
    id='2b895c53-7c64-454e-bb0b-34896c3ca5ac',
    mtu=963741,
    on_backpressure=shared.OutputStatsdExtBackpressureBehavior.BLOCK,
    pipeline='vero',
    port=141506,
    pq_compress=shared.OutputStatsdExtCompression.GZIP,
    pq_controls=shared.OutputStatsdExtPqControls(),
    pq_max_file_size='pariatur',
    pq_max_size='nemo',
    pq_on_backpressure=shared.OutputStatsdExtQueueFullBehavior.BLOCK,
    pq_path='aperiam',
    pq_strict_ordering=False,
    protocol=shared.OutputStatsdExtDestinationProtocol.TCP,
    streamtags=[
        'odio',
    ],
    system_fields=[
        'minima',
    ],
    throttle_rate_per_sec='in',
    type=shared.OutputStatsdExtType.STATSD_EXT,
    write_timeout=496915,
)

res = s.output_object.create(req)

if res.outputs is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateOutputObjectResponse](../../models/operations/createoutputobjectresponse.md)**

