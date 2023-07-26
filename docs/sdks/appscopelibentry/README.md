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

req = operations.DeleteAppscopeLibEntryRequest(
    id='fce953f7-3ef7-4fbc-babd-74dd39c0f5d2',
)

res = s.appscope_lib_entry.delete(req)

if res.appscope_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteAppscopeLibEntryRequest](../../models/operations/deleteappscopelibentryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


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

req = operations.GetAppscopeLibEntryRequest(
    id='cff7c70a-4562-46d4-b681-3f16d9f5fce6',
)

res = s.appscope_lib_entry.get(req)

if res.appscope_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAppscopeLibEntryRequest](../../models/operations/getappscopelibentryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


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

req = operations.UpdateAppscopeLibEntryRequest(
    appscope_lib_entry=shared.AppscopeLibEntry(
        config=shared.AppscopeConfigWithCustom(
            cribl=shared.AppscopeConfigWithCustomCribl(
                authtoken='impedit',
                enable=False,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.LINE,
                    host='veniam',
                    path='aliquid',
                    port=81101,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='magnam',
                        enable=False,
                        validateserver=False,
                    ),
                    type='ea',
                ),
                use_scope_source_transport=False,
            ),
            custom=[
                shared.AppscopeCustom(
                    ancestor='consectetur',
                    arg='recusandae',
                    config=shared.AppscopeConfig(
                        cribl=shared.AppscopeConfigCribl(
                            authtoken='aspernatur',
                            enable=False,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='eaque',
                                path='a',
                                port=725595,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='aut',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='aut',
                            ),
                            use_scope_source_transport=False,
                        ),
                        event=shared.AppscopeConfigEvent(
                            enable=False,
                            format=shared.AppscopeConfigEventFormat(
                                enhancefs=False,
                                maxeventpersec=533466,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='aliquam',
                                path='fugit',
                                port=882860,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='inventore',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='non',
                            ),
                            type=shared.AppscopeConfigEventType.NDJSON,
                            watch=[
                                shared.AppscopeConfigEventWatch(
                                    allowbinary=False,
                                    enabled=False,
                                    field='dolorum',
                                    headers='laborum',
                                    name='Lee Kemmer',
                                    type='quas',
                                    value='assumenda',
                                ),
                            ],
                        ),
                        libscope=shared.AppscopeConfigLibscope(
                            commanddir='nulla',
                            configevent=False,
                            log=shared.AppscopeConfigLibscopeLog(
                                level=shared.AppscopeConfigLibscopeLogLevel.INFO,
                                transport=shared.AppscopeTransport(
                                    buffer=shared.AppscopeTransportBuffer.FULL,
                                    host='quasi',
                                    path='tempora',
                                    port=256139,
                                    tls=shared.AppscopeTransportTLS(
                                        cacertpath='explicabo',
                                        enable=False,
                                        validateserver=False,
                                    ),
                                    type='provident',
                                ),
                            ),
                            summaryperiod=55374,
                        ),
                        metric=shared.AppscopeConfigMetric(
                            enable=False,
                            format=shared.AppscopeConfigMetricFormat(
                                statsdmaxlen=476477,
                                statsdprefix='magnam',
                                type='odio',
                                verbosity=262118,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='esse',
                                path='rem',
                                port=683282,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='reprehenderit',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='quidem',
                            ),
                            watch=[
                                'ut',
                                'eum',
                                'suscipit',
                                'assumenda',
                            ],
                        ),
                        payload=shared.AppscopeConfigPayload(
                            dir='eos',
                            enable=False,
                        ),
                        protocol=[
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=788546,
                                name='Angela Olson',
                                payload=False,
                                regex='quo',
                            ),
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=847276,
                                name='Wilbur Gerlach',
                                payload=False,
                                regex='ab',
                            ),
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=587600,
                                name='Rhonda Toy',
                                payload=False,
                                regex='sequi',
                            ),
                        ],
                        tags=[
                            shared.AppscopeConfigTags(
                                key='esse',
                                value='recusandae',
                            ),
                            shared.AppscopeConfigTags(
                                key='aperiam',
                                value='distinctio',
                            ),
                            shared.AppscopeConfigTags(
                                key='quod',
                                value='dignissimos',
                            ),
                            shared.AppscopeConfigTags(
                                key='inventore',
                                value='nihil',
                            ),
                        ],
                    ),
                    env='totam',
                    hostname='uncommon-encounter.info',
                    procname='occaecati',
                    username='Harvey64',
                ),
                shared.AppscopeCustom(
                    ancestor='molestiae',
                    arg='accusantium',
                    config=shared.AppscopeConfig(
                        cribl=shared.AppscopeConfigCribl(
                            authtoken='porro',
                            enable=False,
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
                            use_scope_source_transport=False,
                        ),
                        event=shared.AppscopeConfigEvent(
                            enable=False,
                            format=shared.AppscopeConfigEventFormat(
                                enhancefs=False,
                                maxeventpersec=681393,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='incidunt',
                                path='atque',
                                port=128860,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='minima',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='nisi',
                            ),
                            type=shared.AppscopeConfigEventType.NDJSON,
                            watch=[
                                shared.AppscopeConfigEventWatch(
                                    allowbinary=False,
                                    enabled=False,
                                    field='sapiente',
                                    headers='consequuntur',
                                    name='Rose Turner',
                                    type='et',
                                    value='esse',
                                ),
                            ],
                        ),
                        libscope=shared.AppscopeConfigLibscope(
                            commanddir='eveniet',
                            configevent=False,
                            log=shared.AppscopeConfigLibscopeLog(
                                level=shared.AppscopeConfigLibscopeLogLevel.NONE,
                                transport=shared.AppscopeTransport(
                                    buffer=shared.AppscopeTransportBuffer.LINE,
                                    host='esse',
                                    path='quod',
                                    port=724168,
                                    tls=shared.AppscopeTransportTLS(
                                        cacertpath='vero',
                                        enable=False,
                                        validateserver=False,
                                    ),
                                    type='aliquid',
                                ),
                            ),
                            summaryperiod=93459,
                        ),
                        metric=shared.AppscopeConfigMetric(
                            enable=False,
                            format=shared.AppscopeConfigMetricFormat(
                                statsdmaxlen=904045,
                                statsdprefix='vel',
                                type='harum',
                                verbosity=473221,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='occaecati',
                                path='minima',
                                port=716244,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='eligendi',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='sit',
                            ),
                            watch=[
                                'tempore',
                                'adipisci',
                                'cumque',
                            ],
                        ),
                        payload=shared.AppscopeConfigPayload(
                            dir='consequuntur',
                            enable=False,
                        ),
                        protocol=[
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=796392,
                                name='Miranda Feest',
                                payload=False,
                                regex='provident',
                            ),
                        ],
                        tags=[
                            shared.AppscopeConfigTags(
                                key='nulla',
                                value='quas',
                            ),
                            shared.AppscopeConfigTags(
                                key='esse',
                                value='quasi',
                            ),
                            shared.AppscopeConfigTags(
                                key='a',
                                value='error',
                            ),
                            shared.AppscopeConfigTags(
                                key='sint',
                                value='pariatur',
                            ),
                        ],
                    ),
                    env='possimus',
                    hostname='cuddly-timpani.org',
                    procname='facere',
                    username='Arvel62',
                ),
                shared.AppscopeCustom(
                    ancestor='culpa',
                    arg='aliquid',
                    config=shared.AppscopeConfig(
                        cribl=shared.AppscopeConfigCribl(
                            authtoken='tenetur',
                            enable=False,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='earum',
                                path='vel',
                                port=447378,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='eius',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='libero',
                            ),
                            use_scope_source_transport=False,
                        ),
                        event=shared.AppscopeConfigEvent(
                            enable=False,
                            format=shared.AppscopeConfigEventFormat(
                                enhancefs=False,
                                maxeventpersec=849039,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='accusantium',
                                path='aliquam',
                                port=958983,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='dicta',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='ullam',
                            ),
                            type=shared.AppscopeConfigEventType.NDJSON,
                            watch=[
                                shared.AppscopeConfigEventWatch(
                                    allowbinary=False,
                                    enabled=False,
                                    field='ullam',
                                    headers='nisi',
                                    name='Nora Denesik',
                                    type='deleniti',
                                    value='itaque',
                                ),
                                shared.AppscopeConfigEventWatch(
                                    allowbinary=False,
                                    enabled=False,
                                    field='dolorum',
                                    headers='architecto',
                                    name='Irvin Boyle III',
                                    type='ipsa',
                                    value='minima',
                                ),
                            ],
                        ),
                        libscope=shared.AppscopeConfigLibscope(
                            commanddir='veritatis',
                            configevent=False,
                            log=shared.AppscopeConfigLibscopeLog(
                                level=shared.AppscopeConfigLibscopeLogLevel.INFO,
                                transport=shared.AppscopeTransport(
                                    buffer=shared.AppscopeTransportBuffer.LINE,
                                    host='iste',
                                    path='temporibus',
                                    port=33074,
                                    tls=shared.AppscopeTransportTLS(
                                        cacertpath='rem',
                                        enable=False,
                                        validateserver=False,
                                    ),
                                    type='aut',
                                ),
                            ),
                            summaryperiod=513075,
                        ),
                        metric=shared.AppscopeConfigMetric(
                            enable=False,
                            format=shared.AppscopeConfigMetricFormat(
                                statsdmaxlen=428796,
                                statsdprefix='mollitia',
                                type='ab',
                                verbosity=544591,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='voluptatem',
                                path='dolor',
                                port=580152,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='numquam',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='impedit',
                            ),
                            watch=[
                                'voluptas',
                            ],
                        ),
                        payload=shared.AppscopeConfigPayload(
                            dir='aut',
                            enable=False,
                        ),
                        protocol=[
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=115484,
                                name='Wendell Frami',
                                payload=False,
                                regex='asperiores',
                            ),
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=45659,
                                name='Bertha Cruickshank',
                                payload=False,
                                regex='maxime',
                            ),
                        ],
                        tags=[
                            shared.AppscopeConfigTags(
                                key='officia',
                                value='asperiores',
                            ),
                            shared.AppscopeConfigTags(
                                key='nemo',
                                value='quae',
                            ),
                        ],
                    ),
                    env='quaerat',
                    hostname='spanish-show-stopper.biz',
                    procname='ab',
                    username='Dayton.Paucek',
                ),
                shared.AppscopeCustom(
                    ancestor='velit',
                    arg='culpa',
                    config=shared.AppscopeConfig(
                        cribl=shared.AppscopeConfigCribl(
                            authtoken='est',
                            enable=False,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='totam',
                                path='fugiat',
                                port=424089,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='ducimus',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='quos',
                            ),
                            use_scope_source_transport=False,
                        ),
                        event=shared.AppscopeConfigEvent(
                            enable=False,
                            format=shared.AppscopeConfigEventFormat(
                                enhancefs=False,
                                maxeventpersec=427834,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='possimus',
                                path='facilis',
                                port=738227,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='commodi',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='in',
                            ),
                            type=shared.AppscopeConfigEventType.NDJSON,
                            watch=[
                                shared.AppscopeConfigEventWatch(
                                    allowbinary=False,
                                    enabled=False,
                                    field='reiciendis',
                                    headers='assumenda',
                                    name='Miss Sophie Jacobi',
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
                            ],
                        ),
                        libscope=shared.AppscopeConfigLibscope(
                            commanddir='dolore',
                            configevent=False,
                            log=shared.AppscopeConfigLibscopeLog(
                                level=shared.AppscopeConfigLibscopeLogLevel.DEBUG,
                                transport=shared.AppscopeTransport(
                                    buffer=shared.AppscopeTransportBuffer.FULL,
                                    host='adipisci',
                                    path='non',
                                    port=228263,
                                    tls=shared.AppscopeTransportTLS(
                                        cacertpath='beatae',
                                        enable=False,
                                        validateserver=False,
                                    ),
                                    type='dignissimos',
                                ),
                            ),
                            summaryperiod=950953,
                        ),
                        metric=shared.AppscopeConfigMetric(
                            enable=False,
                            format=shared.AppscopeConfigMetricFormat(
                                statsdmaxlen=891523,
                                statsdprefix='consectetur',
                                type='corporis',
                                verbosity=689768,
                            ),
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='ipsa',
                                path='voluptates',
                                port=730709,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='vitae',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='accusamus',
                            ),
                            watch=[
                                'tempora',
                                'aspernatur',
                                'voluptas',
                            ],
                        ),
                        payload=shared.AppscopeConfigPayload(
                            dir='voluptas',
                            enable=False,
                        ),
                        protocol=[
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=324405,
                                name='Wilbur Ferry',
                                payload=False,
                                regex='blanditiis',
                            ),
                            shared.AppscopeConfigProtocol(
                                binary=False,
                                detect=False,
                                len=449292,
                                name='Suzanne Torphy',
                                payload=False,
                                regex='adipisci',
                            ),
                        ],
                        tags=[
                            shared.AppscopeConfigTags(
                                key='blanditiis',
                                value='quas',
                            ),
                            shared.AppscopeConfigTags(
                                key='hic',
                                value='nesciunt',
                            ),
                            shared.AppscopeConfigTags(
                                key='culpa',
                                value='corrupti',
                            ),
                        ],
                    ),
                    env='pariatur',
                    hostname='mature-underneath.info',
                    procname='nobis',
                    username='Alberto96',
                ),
            ],
            event=shared.AppscopeConfigWithCustomEvent(
                enable=False,
                format=shared.AppscopeConfigWithCustomEventFormat(
                    enhancefs=False,
                    maxeventpersec=131852,
                ),
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='facilis',
                    path='voluptate',
                    port=709072,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='ab',
                        enable=False,
                        validateserver=False,
                    ),
                    type='iste',
                ),
                type=shared.AppscopeConfigWithCustomEventType.NDJSON,
                watch=[
                    shared.AppscopeConfigWithCustomEventWatch(
                        allowbinary=False,
                        enabled=False,
                        field='laborum',
                        headers='sed',
                        name='Tonya Predovic',
                        type='unde',
                        value='architecto',
                    ),
                    shared.AppscopeConfigWithCustomEventWatch(
                        allowbinary=False,
                        enabled=False,
                        field='suscipit',
                        headers='sapiente',
                        name='Ms. Gregory Wisoky',
                        type='incidunt',
                        value='sed',
                    ),
                ],
            ),
            libscope=shared.AppscopeConfigWithCustomLibscope(
                commanddir='provident',
                configevent=False,
                log=shared.AppscopeConfigWithCustomLibscopeLog(
                    level=shared.AppscopeConfigWithCustomLibscopeLogLevel.INFO,
                    transport=shared.AppscopeTransport(
                        buffer=shared.AppscopeTransportBuffer.FULL,
                        host='ipsum',
                        path='ea',
                        port=579912,
                        tls=shared.AppscopeTransportTLS(
                            cacertpath='quos',
                            enable=False,
                            validateserver=False,
                        ),
                        type='voluptatibus',
                    ),
                ),
                summaryperiod=271653,
            ),
            metric=shared.AppscopeConfigWithCustomMetric(
                enable=False,
                format=shared.AppscopeConfigWithCustomMetricFormat(
                    statsdmaxlen=273009,
                    statsdprefix='voluptate',
                    type='reiciendis',
                    verbosity=401713,
                ),
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.LINE,
                    host='non',
                    path='officiis',
                    port=505866,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='facilis',
                        enable=False,
                        validateserver=False,
                    ),
                    type='quaerat',
                ),
                watch=[
                    'ipsam',
                    'debitis',
                ],
            ),
            payload=shared.AppscopeConfigWithCustomPayload(
                dir='rem',
                enable=False,
            ),
            protocol=[
                shared.AppscopeConfigWithCustomProtocol(
                    binary=False,
                    detect=False,
                    len=750595,
                    name='Floyd Harber',
                    payload=False,
                    regex='nulla',
                ),
            ],
            tags=[
                shared.AppscopeConfigWithCustomTags(
                    key='aperiam',
                    value='saepe',
                ),
            ],
        ),
        description='numquam',
        id='57e1858b-6a89-4fbe-ba5a-a8e4824d0ab4',
        lib=shared.CriblLib.CRIBL,
        tags='esse',
    ),
    id='5088e518-6206-45e9-84f3-b1194b8abf60',
)

res = s.appscope_lib_entry.update(req)

if res.appscope_lib_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateAppscopeLibEntryRequest](../../models/operations/updateappscopelibentryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.UpdateAppscopeLibEntryResponse](../../models/operations/updateappscopelibentryresponse.md)**

