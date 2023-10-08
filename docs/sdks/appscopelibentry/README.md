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
    security=shared.Security(
        bearer_auth="",
    ),
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
                                type='Configuration Money',
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
                            'blue',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='grey technology East',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=169727,
                            name='Northwest',
                            payload=False,
                            regex='SUV quantify Polestar',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='physical Ameliorated',
                        ),
                    ],
                ),
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=259629,
            ),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    type='South Intelligent Fish',
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
                'Buckinghamshire',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='easily',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=415714,
                name='Metal',
                payload=False,
                regex='Direct metrics',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='Minivan',
            ),
        ],
    ),
    description='Universal multimedia architecture',
    id='<ID>',
    lib=shared.CriblLib.CRIBL,
)

res = s.appscope_lib_entry.create(req)

if res.appscope_lib_entry is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.appscope_lib_entry.delete(id='program')

if res.appscope_lib_entry is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.appscope_lib_entry.get(id='female')

if res.appscope_lib_entry is not None:
    # handle response
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
    security=shared.Security(
        bearer_auth="",
    ),
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
                                type='male Metal',
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
                            'cheater',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='Cotton',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=311507,
                            name='Plastic Carolina syndicate',
                            payload=False,
                            regex='implement JBOD',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='Quality guestbook driver',
                        ),
                    ],
                ),
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=338819,
            ),
            transport=shared.AppscopeTransport(
                tls=shared.AppscopeTransportTLS(),
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    type='Sharable Division Northeast',
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
                'Wooden',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='Jaguar Dodge',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=888006,
                name='female',
                payload=False,
                regex='frictionless haptic',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='possimus navigating Diesel',
            ),
        ],
    ),
    description='Centralized bottom-line capability',
    id='<ID>',
    lib=shared.CriblLib.CUSTOM,
))

if res.appscope_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique ID                                                                    |
| `appscope_lib_entry`                                                         | [Optional[shared.AppscopeLibEntry]](../../models/shared/appscopelibentry.md) | :heavy_minus_sign:                                                           | AppscopeLibEntry object to be updated                                        |


### Response

**[operations.UpdateAppscopeLibEntryResponse](../../models/operations/updateappscopelibentryresponse.md)**

