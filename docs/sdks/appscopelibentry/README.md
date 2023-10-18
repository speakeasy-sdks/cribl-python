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
                                type='bluetooth',
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
                            'Extended',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='South',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=996706,
                            name='grey',
                            payload=False,
                            regex='technology',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='East',
                        ),
                    ],
                ),
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=169727,
            ),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    type='evolve',
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
                'male',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='SUV',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=551929,
                name='Screen',
                payload=False,
                regex='mobile',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='National',
            ),
        ],
    ),
    description='Ameliorated demand-driven superstructure',
    id='<ID>',
    lib=shared.CriblLib.CRIBL,
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


res = s.appscope_lib_entry.delete(id='program')

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


res = s.appscope_lib_entry.get(id='female')

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


res = s.appscope_lib_entry.update(id='Van', appscope_lib_entry=shared.AppscopeLibEntry(
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
                            maxeventpersec=15652,
                        ),
                        transport=shared.AppscopeTransport(
                            tls=shared.AppscopeTransportTLS(),
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                type='Reactive',
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
                            'dock',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='Quality',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=488852,
                            name='invoice',
                            payload=False,
                            regex='Arizona',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='Cotton',
                        ),
                    ],
                ),
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=311507,
            ),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    type='white',
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
                'bifurcated',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='Forward',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=993680,
                name='immediately',
                payload=False,
                regex='implement',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='JBOD',
            ),
        ],
    ),
    description='Robust modular open system',
    id='<ID>',
    lib=shared.CriblLib.CUSTOM,
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

