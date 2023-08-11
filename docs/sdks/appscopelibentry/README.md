# appscope_lib_entry

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
            authtoken='corrupti',
            enable=False,
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='distinctio',
                path='quibusdam',
                port=602763,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='nulla',
                    enable=False,
                    validateserver=False,
                ),
                type='corrupti',
            ),
            use_scope_source_transport=False,
        ),
        custom=[
            shared.AppscopeCustom(
                ancestor='vel',
                arg='error',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='deserunt',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='iure',
                            path='magnam',
                            port=891773,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='ipsa',
                                enable=False,
                                validateserver=False,
                            ),
                            type='delectus',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=272656,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='molestiae',
                            path='minus',
                            port=812169,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='voluptatum',
                                enable=False,
                                validateserver=False,
                            ),
                            type='iusto',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='nisi',
                                headers='recusandae',
                                name='Miss Raymond Hauck III',
                                type='repellendus',
                                value='sapiente',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='quo',
                                headers='odit',
                                name='Wilfred Wolff',
                                type='quod',
                                value='esse',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='totam',
                                headers='porro',
                                name='Samuel Reichel',
                                type='fugit',
                                value='deleniti',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='hic',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.ERROR,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='beatae',
                                path='commodi',
                                port=473600,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='modi',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='qui',
                            ),
                        ),
                        summaryperiod=774234,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=736918,
                            statsdprefix='esse',
                            type='ipsum',
                            verbosity=568434,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='perferendis',
                            path='ad',
                            port=617636,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='sed',
                                enable=False,
                                validateserver=False,
                            ),
                            type='iste',
                        ),
                        watch=[
                            'natus',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='laboriosam',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=902599,
                            name='Harvey Hessel',
                            payload=False,
                            regex='saepe',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=697631,
                            name='Brenda Wisozk',
                            payload=False,
                            regex='laborum',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=170909,
                            name='Stacy Champlin',
                            payload=False,
                            regex='omnis',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=363711,
                            name='Velma Batz',
                            payload=False,
                            regex='doloribus',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='architecto',
                            value='mollitia',
                        ),
                        shared.AppscopeConfigTags(
                            key='dolorem',
                            value='culpa',
                        ),
                        shared.AppscopeConfigTags(
                            key='consequuntur',
                            value='repellat',
                        ),
                        shared.AppscopeConfigTags(
                            key='mollitia',
                            value='occaecati',
                        ),
                    ],
                ),
                env='numquam',
                hostname='immediate-instructor.info',
                procname='velit',
                username='Linda.Cronin',
            ),
            shared.AppscopeCustom(
                ancestor='laborum',
                arg='animi',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='enim',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='quo',
                            path='sequi',
                            port=949572,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='ipsam',
                                enable=False,
                                validateserver=False,
                            ),
                            type='id',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=820994,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='quasi',
                            path='error',
                            port=837945,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='laborum',
                                enable=False,
                                validateserver=False,
                            ),
                            type='quasi',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='voluptatibus',
                                headers='vero',
                                name='Miss Irma Wolff',
                                type='cum',
                                value='perferendis',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='doloremque',
                                headers='reprehenderit',
                                name='Shawna Carter',
                                type='iusto',
                                value='dicta',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='harum',
                                headers='enim',
                                name='Mrs. Leslie VonRueden',
                                type='molestias',
                                value='excepturi',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='pariatur',
                                headers='modi',
                                name='Dr. Jordan Von',
                                type='veritatis',
                                value='itaque',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='incidunt',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.INFO,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='est',
                                path='quibusdam',
                                port=131797,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='deserunt',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='distinctio',
                            ),
                        ),
                        summaryperiod=841386,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=289406,
                            statsdprefix='modi',
                            type='qui',
                            verbosity=397821,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='quos',
                            path='perferendis',
                            port=164940,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='assumenda',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ipsam',
                        ),
                        watch=[
                            'fugit',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='dolorum',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=270008,
                            name='Geoffrey Green',
                            payload=False,
                            regex='non',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=756107,
                            name='Gilbert Medhurst',
                            payload=False,
                            regex='officia',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=223081,
                            name='Randal Parisian',
                            payload=False,
                            regex='illum',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='rerum',
                            value='dicta',
                        ),
                        shared.AppscopeConfigTags(
                            key='magnam',
                            value='cumque',
                        ),
                        shared.AppscopeConfigTags(
                            key='facere',
                            value='ea',
                        ),
                        shared.AppscopeConfigTags(
                            key='aliquid',
                            value='laborum',
                        ),
                    ],
                ),
                env='accusamus',
                hostname='exemplary-mover.biz',
                procname='accusamus',
                username='Virgil_Pouros',
            ),
            shared.AppscopeCustom(
                ancestor='id',
                arg='blanditiis',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='deleniti',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='amet',
                            path='deserunt',
                            port=394869,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='vel',
                                enable=False,
                                validateserver=False,
                            ),
                            type='natus',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=606393,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='perferendis',
                            path='nihil',
                            port=301575,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='distinctio',
                                enable=False,
                                validateserver=False,
                            ),
                            type='id',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='labore',
                                headers='suscipit',
                                name='Robin Keebler',
                                type='architecto',
                                value='magnam',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='et',
                                headers='excepturi',
                                name='Ramona Lueilwitz MD',
                                type='reiciendis',
                                value='mollitia',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='ad',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.WARNING,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='necessitatibus',
                                path='odit',
                                port=367562,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='quasi',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='iure',
                            ),
                        ),
                        summaryperiod=984043,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=891924,
                            statsdprefix='eius',
                            type='maxime',
                            verbosity=537023,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='in',
                            path='architecto',
                            port=99569,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='repudiandae',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ullam',
                        ),
                        watch=[
                            'nihil',
                            'repellat',
                            'quibusdam',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='sed',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=868126,
                            name='Kathryn Lang',
                            payload=False,
                            regex='sunt',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=779051,
                            name='Ervin Schoen',
                            payload=False,
                            regex='odit',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=407183,
                            name='Virginia Wunsch',
                            payload=False,
                            regex='voluptate',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=420075,
                            name='Gary Streich',
                            payload=False,
                            regex='perferendis',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='amet',
                            value='aut',
                        ),
                        shared.AppscopeConfigTags(
                            key='cumque',
                            value='corporis',
                        ),
                        shared.AppscopeConfigTags(
                            key='hic',
                            value='libero',
                        ),
                        shared.AppscopeConfigTags(
                            key='nobis',
                            value='dolores',
                        ),
                    ],
                ),
                env='quis',
                hostname='mealy-kilometer.com',
                procname='quis',
                username='Cody17',
            ),
            shared.AppscopeCustom(
                ancestor='minus',
                arg='quam',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='dolor',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='nostrum',
                            path='hic',
                            port=928082,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='omnis',
                                enable=False,
                                validateserver=False,
                            ),
                            type='facilis',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=596656,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='porro',
                            path='consequuntur',
                            port=500026,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='error',
                                enable=False,
                                validateserver=False,
                            ),
                            type='eaque',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='rerum',
                                headers='adipisci',
                                name='Merle Gleichner',
                                type='deleniti',
                                value='pariatur',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='provident',
                                headers='nobis',
                                name='Toby Hahn',
                                type='dolorem',
                                value='dolorem',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='dolor',
                                headers='qui',
                                name='Mindy Marks',
                                type='dignissimos',
                                value='reiciendis',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='amet',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.ERROR,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='veritatis',
                                path='ipsa',
                                port=56418,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='iure',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='odio',
                            ),
                        ),
                        summaryperiod=311796,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=881005,
                            statsdprefix='quidem',
                            type='voluptatibus',
                            verbosity=377752,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='eos',
                            path='atque',
                            port=24678,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='fugiat',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ab',
                        ),
                        watch=[
                            'dolorum',
                            'iusto',
                            'voluptate',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='dolorum',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=607045,
                            name='Kelvin Zboncak',
                            payload=False,
                            regex='voluptate',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=663078,
                            name='Mrs. Ray Collins',
                            payload=False,
                            regex='accusamus',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=320017,
                            name='Sam Oberbrunner',
                            payload=False,
                            regex='repellendus',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='similique',
                            value='alias',
                        ),
                        shared.AppscopeConfigTags(
                            key='at',
                            value='quaerat',
                        ),
                        shared.AppscopeConfigTags(
                            key='tempora',
                            value='vel',
                        ),
                    ],
                ),
                env='quod',
                hostname='uneven-commitment.net',
                procname='a',
                username='Jacky.Pfeffer',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=788740,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='amet',
                path='tempore',
                port=880298,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='numquam',
                    enable=False,
                    validateserver=False,
                ),
                type='enim',
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='sapiente',
                    headers='totam',
                    name='Karen Rath',
                    type='vel',
                    value='libero',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='voluptas',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.ERROR,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.LINE,
                    host='ipsum',
                    path='incidunt',
                    port=186458,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='cupiditate',
                        enable=False,
                        validateserver=False,
                    ),
                    type='maxime',
                ),
            ),
            summaryperiod=863856,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=747080,
                statsdprefix='dicta',
                type='laborum',
                verbosity=517379,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='aspernatur',
                path='dolores',
                port=716860,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='facilis',
                    enable=False,
                    validateserver=False,
                ),
                type='aliquid',
            ),
            watch=[
                'molestias',
                'temporibus',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='qui',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=144847,
                name='Courtney Cassin',
                payload=False,
                regex='hic',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='cumque',
                value='soluta',
            ),
        ],
    ),
    description='nobis',
    id='1e31b8b9-0f34-443a-9108-e0adcf4b9218',
    lib=shared.CriblLib.CRIBL_CUSTOM,
    tags='occaecati',
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


res = s.appscope_lib_entry.delete(id='voluptatibus')

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


res = s.appscope_lib_entry.get(id='quisquam')

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


res = s.appscope_lib_entry.update(id='vero', appscope_lib_entry=shared.AppscopeLibEntry(
    config=shared.AppscopeConfigWithCustom(
        cribl=shared.AppscopeConfigWithCustomCribl(
            authtoken='omnis',
            enable=False,
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='ipsum',
                path='delectus',
                port=455169,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='consectetur',
                    enable=False,
                    validateserver=False,
                ),
                type='vero',
            ),
            use_scope_source_transport=False,
        ),
        custom=[
            shared.AppscopeCustom(
                ancestor='dignissimos',
                arg='hic',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='distinctio',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='odio',
                            path='similique',
                            port=708548,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='vero',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ducimus',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=293020,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='illum',
                            path='sequi',
                            port=617877,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='impedit',
                                enable=False,
                                validateserver=False,
                            ),
                            type='aut',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='exercitationem',
                                headers='nulla',
                                name='Johnnie Wunsch',
                                type='eligendi',
                                value='ducimus',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='alias',
                                headers='officia',
                                name='Roberta Jenkins',
                                type='possimus',
                                value='magnam',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='ratione',
                                headers='ex',
                                name='Willie Fahey III',
                                type='nulla',
                                value='excepturi',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='voluptatibus',
                                headers='nostrum',
                                name='Devin Ullrich',
                                type='corporis',
                                value='veniam',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='aliquid',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.DEBUG,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='ea',
                                path='quo',
                                port=232234,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='recusandae',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='aspernatur',
                            ),
                        ),
                        summaryperiod=325310,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=53427,
                            statsdprefix='a',
                            type='libero',
                            verbosity=13948,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='deleniti',
                            path='impedit',
                            port=304582,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='fugit',
                                enable=False,
                                validateserver=False,
                            ),
                            type='accusamus',
                        ),
                        watch=[
                            'non',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='et',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=672048,
                            name='Lee Kemmer',
                            payload=False,
                            regex='quas',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=829603,
                            name='Mrs. Shane Reinger',
                            payload=False,
                            regex='explicabo',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=591935,
                            name='Minnie Gutkowski',
                            payload=False,
                            regex='esse',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='rem',
                            value='fuga',
                        ),
                        shared.AppscopeConfigTags(
                            key='reprehenderit',
                            value='quidem',
                        ),
                    ],
                ),
                env='fugiat',
                hostname='firm-honoree.info',
                procname='assumenda',
                username='Chet.Lang5',
            ),
            shared.AppscopeCustom(
                ancestor='id',
                arg='quidem',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='neque',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='illum',
                            path='quo',
                            port=681359,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='eius',
                                enable=False,
                                validateserver=False,
                            ),
                            type='eos',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=373813,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='cupiditate',
                            path='consequatur',
                            port=272822,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='debitis',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ipsam',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='sequi',
                                headers='quo',
                                name='Sophie Bayer',
                                type='dignissimos',
                                value='inventore',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='nihil',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.WARNING,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='aliquam',
                                path='odio',
                                port=577543,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='commodi',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='sapiente',
                            ),
                        ),
                        summaryperiod=174112,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=645570,
                            statsdprefix='molestiae',
                            type='accusantium',
                            verbosity=783648,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='quas',
                            path='praesentium',
                            port=159867,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='deleniti',
                                enable=False,
                                validateserver=False,
                            ),
                            type='fugit',
                        ),
                        watch=[
                            'mollitia',
                            'incidunt',
                            'atque',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='explicabo',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=392676,
                            name='Jeannie Cronin',
                            payload=False,
                            regex='saepe',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=578922,
                            name='Carl Koch',
                            payload=False,
                            regex='veritatis',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='quod',
                            value='nam',
                        ),
                        shared.AppscopeConfigTags(
                            key='vero',
                            value='aliquid',
                        ),
                    ],
                ),
                env='quasi',
                hostname='untidy-heterosexual.net',
                procname='molestiae',
                username='Maximus71',
            ),
            shared.AppscopeCustom(
                ancestor='eligendi',
                arg='sit',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='culpa',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='adipisci',
                            path='cumque',
                            port=160538,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='consequatur',
                                enable=False,
                                validateserver=False,
                            ),
                            type='minus',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=308286,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='consectetur',
                            path='esse',
                            port=503427,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='provident',
                                enable=False,
                                validateserver=False,
                            ),
                            type='a',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='quas',
                                headers='esse',
                                name='Lorene Mueller',
                                type='possimus',
                                value='quia',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='eveniet',
                                headers='asperiores',
                                name='Miss Peter Cronin',
                                type='aliquid',
                                value='tenetur',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='quae',
                                headers='earum',
                                name='Pearl Gerlach',
                                type='soluta',
                                value='accusantium',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='aliquam',
                                headers='sapiente',
                                name='Marion Kihn',
                                type='aut',
                                value='voluptatum',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='qui',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.NONE,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='deleniti',
                                path='itaque',
                                port=680270,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='architecto',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='omnis',
                            ),
                        ),
                        summaryperiod=945302,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=98478,
                            statsdprefix='at',
                            type='et',
                            verbosity=454162,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='minima',
                            path='veritatis',
                            port=232744,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='adipisci',
                                enable=False,
                                validateserver=False,
                            ),
                            type='iste',
                        ),
                        watch=[
                            'accusantium',
                            'rem',
                            'aut',
                            'laudantium',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='eum',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=68074,
                            name='Kyle Bartoletti',
                            payload=False,
                            regex='numquam',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=771089,
                            name='Loretta Anderson DVM',
                            payload=False,
                            regex='natus',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=244651,
                            name='Ms. Glen Zboncak',
                            payload=False,
                            regex='consequuntur',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='officia',
                            value='maxime',
                        ),
                        shared.AppscopeConfigTags(
                            key='dignissimos',
                            value='officia',
                        ),
                        shared.AppscopeConfigTags(
                            key='asperiores',
                            value='nemo',
                        ),
                        shared.AppscopeConfigTags(
                            key='quae',
                            value='quaerat',
                        ),
                    ],
                ),
                env='porro',
                hostname='steep-dumbwaiter.com',
                procname='adipisci',
                username='Mark.Ondricka',
            ),
            shared.AppscopeCustom(
                ancestor='culpa',
                arg='est',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='recusandae',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='fugiat',
                            path='vel',
                            port=497678,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='quos',
                                enable=False,
                                validateserver=False,
                            ),
                            type='vel',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=287051,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='facilis',
                            path='cum',
                            port=414857,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='in',
                                enable=False,
                                validateserver=False,
                            ),
                            type='corporis',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='assumenda',
                                headers='nemo',
                                name='Gilbert Bayer',
                                type='in',
                                value='exercitationem',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='earum',
                                headers='facere',
                                name='Melba Homenick',
                                type='saepe',
                                value='necessitatibus',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='dolore',
                                headers='sunt',
                                name='Chad Franey IV',
                                type='a',
                                value='debitis',
                            ),
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='consectetur',
                                headers='corporis',
                                name='Rick Beer',
                                type='vitae',
                                value='accusamus',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='similique',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.INFO,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='voluptas',
                                path='voluptas',
                                port=374296,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='minima',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='nobis',
                            ),
                        ),
                        summaryperiod=680116,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=237807,
                            statsdprefix='minus',
                            type='dolores',
                            verbosity=503934,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='dolore',
                            path='aliquam',
                            port=885963,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='temporibus',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ullam',
                        ),
                        watch=[
                            'cum',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='blanditiis',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=942584,
                            name='Molly Lowe',
                            payload=False,
                            regex='hic',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=348783,
                            name='Paul Price',
                            payload=False,
                            regex='explicabo',
                        ),
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=994401,
                            name='Miss Jared Quitzon',
                            payload=False,
                            regex='laborum',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='in',
                            value='commodi',
                        ),
                    ],
                ),
                env='quidem',
                hostname='common-gather.name',
                procname='architecto',
                username='Geovany.Willms96',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=19300,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='maiores',
                path='incidunt',
                port=148478,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='provident',
                    enable=False,
                    validateserver=False,
                ),
                type='eius',
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='ipsum',
                    headers='ea',
                    name='Isaac Wolf',
                    type='voluptate',
                    value='reiciendis',
                ),
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='ex',
                    headers='sit',
                    name='Cecelia Lakin',
                    type='incidunt',
                    value='ipsam',
                ),
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='debitis',
                    headers='rem',
                    name='Della Muller',
                    type='recusandae',
                    value='reiciendis',
                ),
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='nulla',
                    headers='magni',
                    name='Gwen Fritsch',
                    type='officiis',
                    value='beatae',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='laudantium',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.INFO,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='cum',
                    path='laboriosam',
                    port=680515,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='voluptatum',
                        enable=False,
                        validateserver=False,
                    ),
                    type='error',
                ),
            ),
            summaryperiod=944708,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=710529,
                statsdprefix='debitis',
                type='neque',
                verbosity=677115,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='officia',
                path='dolorum',
                port=548361,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='accusamus',
                    enable=False,
                    validateserver=False,
                ),
                type='tempora',
            ),
            watch=[
                'fugit',
                'ut',
                'fugiat',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='voluptatem',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=710337,
                name='Barbara Koelpin IV',
                payload=False,
                regex='quas',
            ),
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=922112,
                name='Janet Kuvalis',
                payload=False,
                regex='sit',
            ),
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=425508,
                name='Mrs. Tricia Mueller',
                payload=False,
                regex='dolorem',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='dicta',
                value='architecto',
            ),
            shared.AppscopeConfigWithCustomTags(
                key='occaecati',
                value='labore',
            ),
            shared.AppscopeConfigWithCustomTags(
                key='quidem',
                value='atque',
            ),
        ],
    ),
    description='laborum',
    id='bf603a79-f9df-4e0a-b7da-8a50ce187f86',
    lib=shared.CriblLib.CUSTOM,
    tags='maxime',
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

