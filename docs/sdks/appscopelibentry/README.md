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
            authtoken='bluetooth Extended',
            enable=False,
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='speedy-basil.org',
                path='/usr/local/bin',
                port=376844,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='abnormally deposit evolve',
                    enable=False,
                    validateserver=False,
                ),
                type='fuchsia Gasoline Screen',
            ),
            use_scope_source_transport=False,
        ),
        custom=[
            shared.AppscopeCustom(
                ancestor='physical Ameliorated',
                arg='after',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='Intelligent Fish',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='sweaty-executor.org',
                            path='/home',
                            port=415714,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='Metal',
                                enable=False,
                                validateserver=False,
                            ),
                            type='Direct metrics',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=36521,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='petty-tool.name',
                            path='/dev',
                            port=200664,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='West',
                                enable=False,
                                validateserver=False,
                            ),
                            type='Towels likewise',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='Praseodymium Bicycle',
                                headers='choke Sausages lavender',
                                name='Lake Dollar Electronic',
                                type='pink Southwest',
                                value='Mongolia Maine sexy',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='Garden Electric',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.ERROR,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='sarcastic-competition.name',
                                path='/usr/local/src',
                                port=445608,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='Lead Wagon telecast',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='program East Outdoors',
                            ),
                        ),
                        summaryperiod=844162,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=675289,
                            statsdprefix='District Avon',
                            type='Franc debitis Bacon',
                            verbosity=433224,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='rural-sentence.org',
                            path='/tmp',
                            port=823683,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='Car Functionality',
                                enable=False,
                                validateserver=False,
                            ),
                            type='Minivan',
                        ),
                        watch=[
                            'compressing',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='FTM',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=520049,
                            name='Oganesson Gasoline',
                            payload=False,
                            regex='Oro',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='Extended phew array',
                        ),
                    ],
                ),
                env='South yum',
                hostname='perky-resistance.name',
                procname='Gasoline',
                username='Winfield_Fahey28',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=448849,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='ordinary-populist.biz',
                path='/usr/local/bin',
                port=88424,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Copernicium lux Iran',
                    enable=False,
                    validateserver=False,
                ),
                type='Borders',
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='Soft framework Rustic',
                    headers='neural',
                    name='given Practical',
                    type='mobile Barium Fantastic',
                    value='tan Iowa viral',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='Executive index Northwest',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.INFO,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='yellow-federation.net',
                    path='/var',
                    port=251547,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='Fish',
                        enable=False,
                        validateserver=False,
                    ),
                    type='Californium Passenger',
                ),
            ),
            summaryperiod=440309,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=931588,
                statsdprefix='Plastic Steel water',
                type='beatae SUV',
                verbosity=541340,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='usable-gerbil.net',
                path='/selinux',
                port=790896,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Mouse South voluptatibus',
                    enable=False,
                    validateserver=False,
                ),
                type='Clothing disintermediate',
            ),
            watch=[
                'Kia',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='Minivan Integration unleash',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=676671,
                name='which complexity Electric',
                payload=False,
                regex='Porsche ukulele',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='seldom',
            ),
        ],
    ),
    description='Total tangible frame',
    id='<ID>',
    lib=shared.CriblLib.CUSTOM,
    tags='Automotive',
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
            authtoken='Reactive',
            enable=False,
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='far-off-pamphlet.net',
                path='/private/var',
                port=443076,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Arizona Cotton extend',
                    enable=False,
                    validateserver=False,
                ),
                type='bifurcated',
            ),
            use_scope_source_transport=False,
        ),
        custom=[
            shared.AppscopeCustom(
                ancestor='silver immediately',
                arg='East',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='Bicycle guestbook',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='angelic-fee.net',
                            path='/opt',
                            port=810877,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='Lev Wooden',
                                enable=False,
                                validateserver=False,
                            ),
                            type='Jaguar Dodge',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=888006,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='runny-flower.name',
                            path='/media',
                            port=329712,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='parse possimus',
                                enable=False,
                                validateserver=False,
                            ),
                            type='Turkish Avon',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='hungrily',
                                headers='Global Northeast Xenogender',
                                name='West',
                                type='Southeast',
                                value='Pickup Ergonomic Money',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='Group wank Latvian',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.NONE,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='gullible-horde.org',
                                path='/usr/ports',
                                port=612391,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='tremendously pace',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='Bacon',
                            ),
                        ),
                        summaryperiod=671359,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=727983,
                            statsdprefix='port',
                            type='Tools',
                            verbosity=338673,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='real-salt.biz',
                            path='/lib',
                            port=276135,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='portals',
                                enable=False,
                                validateserver=False,
                            ),
                            type='woot',
                        ),
                        watch=[
                            'Metal',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='primary surprisingly',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=418936,
                            name='Director Assistant',
                            payload=False,
                            regex='Pants',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='RSS Electronic Diesel',
                        ),
                    ],
                ),
                env='van Account',
                hostname='flickering-killing.info',
                procname='leverage Dynamic Plastic',
                username='Audreanne_Goodwin',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=532806,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='sparkling-freighter.name',
                path='/private/tmp',
                port=463392,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Investment',
                    enable=False,
                    validateserver=False,
                ),
                type='absent blockchains',
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='azure',
                    headers='Southwest optical',
                    name='synthesize Hermaphrodite',
                    type='Yen Albania',
                    value='Hybrid',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='City Dinar Southwest',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.WARNING,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='profuse-rumor.net',
                    path='/etc',
                    port=931612,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='San overriding Southeast',
                        enable=False,
                        validateserver=False,
                    ),
                    type='Cove damn Table',
                ),
            ),
            summaryperiod=283611,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=164256,
                statsdprefix='siemens plum',
                type='Russian Optimization Massachusetts',
                verbosity=404545,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='wiry-venture.info',
                path='/opt/lib',
                port=389247,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Bicycle',
                    enable=False,
                    validateserver=False,
                ),
                type='Bronze Dynamic',
            ),
            watch=[
                'grow',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='International Brand',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=875377,
                name='Demigender',
                payload=False,
                regex='midst',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='Heights circuit Metal',
            ),
        ],
    ),
    description='Networked encompassing policy',
    id='<ID>',
    lib=shared.CriblLib.CRIBL,
    tags='Southwest',
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

