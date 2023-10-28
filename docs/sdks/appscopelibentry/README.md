# AppscopeLibEntry
(*appscope_lib_entry*)

### Available Operations

* [create](#create) - Create AppscopeLibEntry
* [delete](#delete) - Delete AppscopeLibEntry
* [get](#get) - Get AppscopeLibEntry by ID
* [update](#update) - Update AppscopeLibEntry

## create

Create AppscopeLibEntry

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    bearer_auth="",
)

req = shared.AppscopeLibEntry(
    config=shared.AppscopeConfigWithCustom(
        cribl=shared.AppscopeConfigWithCustomCribl(
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
        ),
        custom=[
            shared.AppscopeCustom(
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=486589,
                        ),
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                type='string',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        log=shared.AppscopeConfigLibscopeLog(
                            transport=shared.AppscopeTransport(
                                tls=shared.AppscopeTransportTLS(),
                            ),
                        ),
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(),
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                        watch=[
                            'string',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='string',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=489382,
                            name='string',
                            payload=False,
                            regex='string',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='string',
                        ),
                    ],
                ),
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=638424,
            ),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    type='string',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                transport=shared.AppscopeTransport(
                    tls=shared.AppscopeTransportTLS(),
                ),
            ),
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            watch=[
                'string',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='string',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=859213,
                name='string',
                payload=False,
                regex='string',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='string',
            ),
        ],
    ),
    description='Inverse discrete benchmark',
    id='<ID>',
    lib=shared.CriblLib.CUSTOM,
)

res = s.appscope_lib_entry.create(req)

if res.appscope_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.AppscopeLibEntry](../../models/shared/appscopelibentry.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.CreateAppscopeLibEntryResponse](../../models/operations/createappscopelibentryresponse.md)**


## delete

Delete AppscopeLibEntry

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.appscope_lib_entry.delete(id='string')

if res.appscope_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.DeleteAppscopeLibEntryResponse](../../models/operations/deleteappscopelibentryresponse.md)**


## get

Get AppscopeLibEntry by ID

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.appscope_lib_entry.get(id='string')

if res.appscope_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique ID          |


### Response

**[operations.GetAppscopeLibEntryResponse](../../models/operations/getappscopelibentryresponse.md)**


## update

Update AppscopeLibEntry

### Example Usage

```python
import cribl
from cribl.models import operations, shared

s = cribl.Cribl(
    bearer_auth="",
)


res = s.appscope_lib_entry.update(id='string', appscope_lib_entry=shared.AppscopeLibEntry(
    config=shared.AppscopeConfigWithCustom(
        cribl=shared.AppscopeConfigWithCustomCribl(
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
        ),
        custom=[
            shared.AppscopeCustom(
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=857478,
                        ),
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                type='string',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        log=shared.AppscopeConfigLibscopeLog(
                            transport=shared.AppscopeTransport(
                                tls=shared.AppscopeTransportTLS(),
                            ),
                        ),
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(),
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                        watch=[
                            'string',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='string',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=24555,
                            name='string',
                            payload=False,
                            regex='string',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='string',
                        ),
                    ],
                ),
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=597129,
            ),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    type='string',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                transport=shared.AppscopeTransport(
                    tls=shared.AppscopeTransportTLS(),
                ),
            ),
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            watch=[
                'string',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='string',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=15652,
                name='string',
                payload=False,
                regex='string',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='string',
            ),
        ],
    ),
    description='Future-proofed next generation workforce',
    id='<ID>',
    lib=shared.CriblLib.CRIBL,
))

if res.appscope_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique ID                                                                    |
| `appscope_lib_entry`                                                         | [Optional[shared.AppscopeLibEntry]](../../models/shared/appscopelibentry.md) | :heavy_minus_sign:                                                           | AppscopeLibEntry object to be updated                                        |


### Response

**[operations.UpdateAppscopeLibEntryResponse](../../models/operations/updateappscopelibentryresponse.md)**

