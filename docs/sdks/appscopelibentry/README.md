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
                ancestor='illum',
                arg='vel',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='error',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='suscipit',
                            path='iure',
                            port=297534,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='debitis',
                                enable=False,
                                validateserver=False,
                            ),
                            type='ipsa',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=963663,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='suscipit',
                            path='molestiae',
                            port=791725,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='placeat',
                                enable=False,
                                validateserver=False,
                            ),
                            type='voluptatum',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='iusto',
                                headers='excepturi',
                                name='Mrs. Sophie Smith MD',
                                type='perferendis',
                                value='ipsam',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='repellendus',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.NONE,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.FULL,
                                host='odit',
                                path='at',
                                port=870088,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='maiores',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='molestiae',
                            ),
                        ),
                        summaryperiod=799159,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=800911,
                            statsdprefix='esse',
                            type='totam',
                            verbosity=780529,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='dicta',
                            path='nam',
                            port=639921,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='occaecati',
                                enable=False,
                                validateserver=False,
                            ),
                            type='fugit',
                        ),
                        watch=[
                            'deleniti',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='hic',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=758616,
                            name='Jack Johns',
                            payload=False,
                            regex='qui',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='impedit',
                            value='cum',
                        ),
                    ],
                ),
                env='esse',
                hostname='dull-mister.com',
                procname='perferendis',
                username='Enrique61',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=222321,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='laboriosam',
                path='hic',
                port=902599,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='fuga',
                    enable=False,
                    validateserver=False,
                ),
                type='in',
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='corporis',
                    headers='iste',
                    name='Mr. Kerry Predovic',
                    type='est',
                    value='mollitia',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='laborum',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.DEBUG,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.LINE,
                    host='corporis',
                    path='explicabo',
                    port=750686,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='enim',
                        enable=False,
                        validateserver=False,
                    ),
                    type='omnis',
                ),
            ),
            summaryperiod=363711,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=325047,
                statsdprefix='excepturi',
                type='accusantium',
                verbosity=438601,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.FULL,
                host='doloribus',
                path='sapiente',
                port=102044,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='mollitia',
                    enable=False,
                    validateserver=False,
                ),
                type='dolorem',
            ),
            watch=[
                'culpa',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='consequuntur',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=995300,
                name='Tracy Fritsch',
                payload=False,
                regex='molestiae',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='velit',
                value='error',
            ),
        ],
    ),
    description='quia',
    id='51aa52c3-f5ad-4019-9a1f-fe78f097b007',
    lib=shared.CriblLib.CRIBL,
    tags='maiores',
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


res = s.appscope_lib_entry.delete(id='dicta')

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


res = s.appscope_lib_entry.get(id='corporis')

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


res = s.appscope_lib_entry.update(id='dolore', appscope_lib_entry=shared.AppscopeLibEntry(
    config=shared.AppscopeConfigWithCustom(
        cribl=shared.AppscopeConfigWithCustomCribl(
            authtoken='iusto',
            enable=False,
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='harum',
                path='enim',
                port=880476,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='commodi',
                    enable=False,
                    validateserver=False,
                ),
                type='repudiandae',
            ),
            use_scope_source_transport=False,
        ),
        custom=[
            shared.AppscopeCustom(
                ancestor='quae',
                arg='ipsum',
                config=shared.AppscopeConfig(
                    cribl=shared.AppscopeConfigCribl(
                        authtoken='quidem',
                        enable=False,
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.FULL,
                            host='excepturi',
                            path='pariatur',
                            port=265389,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='praesentium',
                                enable=False,
                                validateserver=False,
                            ),
                            type='rem',
                        ),
                        use_scope_source_transport=False,
                    ),
                    event=shared.AppscopeConfigEvent(
                        enable=False,
                        format=shared.AppscopeConfigEventFormat(
                            enhancefs=False,
                            maxeventpersec=916723,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='repudiandae',
                            path='sint',
                            port=83112,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='itaque',
                                enable=False,
                                validateserver=False,
                            ),
                            type='incidunt',
                        ),
                        type=shared.AppscopeConfigEventType.NDJSON,
                        watch=[
                            shared.AppscopeConfigEventWatch(
                                allowbinary=False,
                                enabled=False,
                                field='enim',
                                headers='consequatur',
                                name='Taylor Cole',
                                type='quibusdam',
                                value='labore',
                            ),
                        ],
                    ),
                    libscope=shared.AppscopeConfigLibscope(
                        commanddir='modi',
                        configevent=False,
                        log=shared.AppscopeConfigLibscopeLog(
                            level=shared.AppscopeConfigLibscopeLogLevel.DEBUG,
                            transport=shared.AppscopeTransport(
                                buffer=shared.AppscopeTransportBuffer.LINE,
                                host='cupiditate',
                                path='quos',
                                port=20107,
                                tls=shared.AppscopeTransportTLS(
                                    cacertpath='magni',
                                    enable=False,
                                    validateserver=False,
                                ),
                                type='assumenda',
                            ),
                        ),
                        summaryperiod=369808,
                    ),
                    metric=shared.AppscopeConfigMetric(
                        enable=False,
                        format=shared.AppscopeConfigMetricFormat(
                            statsdmaxlen=4695,
                            statsdprefix='fugit',
                            type='dolorum',
                            verbosity=569618,
                        ),
                        transport=shared.AppscopeTransport(
                            buffer=shared.AppscopeTransportBuffer.LINE,
                            host='facilis',
                            path='tempore',
                            port=288476,
                            tls=shared.AppscopeTransportTLS(
                                cacertpath='delectus',
                                enable=False,
                                validateserver=False,
                            ),
                            type='eum',
                        ),
                        watch=[
                            'non',
                        ],
                    ),
                    payload=shared.AppscopeConfigPayload(
                        dir='eligendi',
                        enable=False,
                    ),
                    protocol=[
                        shared.AppscopeConfigProtocol(
                            binary=False,
                            detect=False,
                            len=576157,
                            name='Sherri Tremblay',
                            payload=False,
                            regex='dolor',
                        ),
                    ],
                    tags=[
                        shared.AppscopeConfigTags(
                            key='debitis',
                            value='a',
                        ),
                    ],
                ),
                env='dolorum',
                hostname='intrepid-ikebana.org',
                procname='maiores',
                username='Maximo76',
            ),
        ],
        event=shared.AppscopeConfigWithCustomEvent(
            enable=False,
            format=shared.AppscopeConfigWithCustomEventFormat(
                enhancefs=False,
                maxeventpersec=813798,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='aliquid',
                path='laborum',
                port=881104,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='non',
                    enable=False,
                    validateserver=False,
                ),
                type='occaecati',
            ),
            type=shared.AppscopeConfigWithCustomEventType.NDJSON,
            watch=[
                shared.AppscopeConfigWithCustomEventWatch(
                    allowbinary=False,
                    enabled=False,
                    field='enim',
                    headers='accusamus',
                    name='Abraham McKenzie',
                    type='blanditiis',
                    value='deleniti',
                ),
            ],
        ),
        libscope=shared.AppscopeConfigWithCustomLibscope(
            commanddir='sapiente',
            configevent=False,
            log=shared.AppscopeConfigWithCustomLibscopeLog(
                level=shared.AppscopeConfigWithCustomLibscopeLogLevel.INFO,
                transport=shared.AppscopeTransport(
                    buffer=shared.AppscopeTransportBuffer.FULL,
                    host='nisi',
                    path='vel',
                    port=618809,
                    tls=shared.AppscopeTransportTLS(
                        cacertpath='omnis',
                        enable=False,
                        validateserver=False,
                    ),
                    type='molestiae',
                ),
            ),
            summaryperiod=19193,
        ),
        metric=shared.AppscopeConfigWithCustomMetric(
            enable=False,
            format=shared.AppscopeConfigWithCustomMetricFormat(
                statsdmaxlen=470132,
                statsdprefix='magnam',
                type='distinctio',
                verbosity=660174,
            ),
            transport=shared.AppscopeTransport(
                buffer=shared.AppscopeTransportBuffer.LINE,
                host='labore',
                path='suscipit',
                port=618016,
                tls=shared.AppscopeTransportTLS(
                    cacertpath='nobis',
                    enable=False,
                    validateserver=False,
                ),
                type='eum',
            ),
            watch=[
                'vero',
            ],
        ),
        payload=shared.AppscopeConfigWithCustomPayload(
            dir='aspernatur',
            enable=False,
        ),
        protocol=[
            shared.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=102863,
                name='Frances Marks',
                payload=False,
                regex='quos',
            ),
        ],
        tags=[
            shared.AppscopeConfigWithCustomTags(
                key='sint',
                value='accusantium',
            ),
        ],
    ),
    description='mollitia',
    id='fa563e25-16fe-44c8-b711-e5b7fd2ed028',
    lib=shared.CriblLib.CRIBL_CUSTOM,
    tags='magni',
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

