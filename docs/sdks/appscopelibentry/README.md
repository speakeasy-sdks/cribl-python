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
                        type='Praseodymium Bicycle',
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='choke Sausages lavender',
                                headers='Lake Dollar Electronic',
                                name='pink Southwest',
                                type='Mongolia Maine sexy',
                                value='Garden Electric',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='Southeast Toys Electric',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.NONE,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='acclaimed-stock.org',
                                path='/var/yp',
                                port=898841,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='program East Outdoors',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='National Executive Franc',
                            ),
                        ),
                        summaryperiod=566512,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=895210,
                            statsdprefix='North',
                            type='Tenge male polish',
                            verbosity=823683,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='drafty-binoculars.name',
                            path='/Library',
                            port=284120,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='MTF Cotton sexy',
                                enable=False,
                                validateserver=False,
                            ),
                            type='Oganesson Gasoline',
                        ),
                        watch=[
                            'Northwest',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='Hybrid Extended',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=929496,
                            name='array bandwidth benchmark',
                            payload=False,
                            regex='velit Gasoline demob',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='ducks deposit Latin',
                        ),
                    ],
                ),
                env='blue',
                hostname='shameful-friend.org',
                procname='risk phooey Savings',
                username='Joey75',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=381603,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='fearful-cinnamon.name',
                path='/media',
                port=328225,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='neural',
                    enable=False,
                    validateserver=False,
                ),
                type='given Practical',
            ),
            type='mobile Barium Fantastic',
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='tan Iowa viral',
                    headers='Executive index Northwest',
                    name='silver mindshare',
                    type='Bronze Fish payment',
                    value='Passenger invoice Gallium',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='Steel water',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.WARNING,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='careless-step-brother.net',
                    path='/root',
                    port=150565,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='productivity quisquam aside',
                        enable=False,
                        validateserver=False,
                    ),
                    type='South',
                ),
            ),
            summaryperiod=575740,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=977591,
                statsdprefix='Clothing disintermediate',
                type='application Minivan Integration',
                verbosity=308370,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='ragged-step.org',
                path='/usr/sbin',
                port=388169,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Electric',
                    enable=False,
                    validateserver=False,
                ),
                type='Porsche ukulele',
            ),
            watch=[
                'Outdoors',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='Total Georgia ugh',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=764307,
                name='South withdrawal',
                payload=False,
                regex='Avon',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='lavender henry',
            ),
        ],
    ),
    description='Centralized homogeneous open system',
    id='<ID>',
    lib=shared.CriblLib.CUSTOM,
    tags='initiatives Rubber Illinois',
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
                        type='hungrily',
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='Global Northeast Xenogender',
                                headers='West',
                                name='Southeast',
                                type='Pickup Ergonomic Money',
                                value='Group wank Latvian',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='Chips Omnigender tremendously',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.NONE,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='full-controller.net',
                                path='/usr',
                                port=727983,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='port',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='Tools',
                            ),
                        ),
                        summaryperiod=338673,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=105402,
                            statsdprefix='Cruiser Electronic woot',
                            type='Berkshire primary',
                            verbosity=883001,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='imperturbable-load.net',
                            path='/Network',
                            port=698876,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='North RSS Electronic',
                                enable=False,
                                validateserver=False,
                            ),
                            type='violet van Account',
                        ),
                        watch=[
                            'interactive',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='orange Baby',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=237592,
                            name='asynchronous',
                            payload=False,
                            regex='bandwidth',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='<key>',
                            value='Oriental leading',
                        ),
                    ],
                ),
                env='killer Manat',
                hostname='wicked-author.biz',
                procname='Charlottesville likewise Southwest',
                username='Jeanie_Stoltenberg',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=674600,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='international-pastoralist.info',
                path='/opt/lib',
                port=44563,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Saginaw',
                    enable=False,
                    validateserver=False,
                ),
                type='Clothing City',
            ),
            type='Luxurious Southwest',
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='Bicycle mole',
                    headers='annually overriding Southeast',
                    name='Cove damn Table',
                    type='violet',
                    value='Convertible Trans Argon',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='bypassing Investment',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.NONE,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='icy-guilt.info',
                    path='/lib',
                    port=777454,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='Division Bronze',
                        enable=False,
                        validateserver=False,
                    ),
                    type='Elegant RAM',
                ),
            ),
            summaryperiod=640672,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=675911,
                statsdprefix='Cambridgeshire North',
                type='midst',
                verbosity=733331,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='sinful-morphology.info',
                path='/System',
                port=527494,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='Metal Chromium Electronic',
                    enable=False,
                    validateserver=False,
                ),
                type='optical deleniti copy',
            ),
            watch=[
                'Shore',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='salmon Beauty Producer',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=359909,
                name='Intelligent invoice hacking',
                payload=False,
                regex='orchid distributed',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='<key>',
                value='Americium',
            ),
        ],
    ),
    description='Right-sized background benchmark',
    id='<ID>',
    lib=shared.CriblLib.CUSTOM,
    tags='circuit',
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

