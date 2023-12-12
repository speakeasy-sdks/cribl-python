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
from cribl.models import components

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = components.AppscopeLibEntry(
    config=components.AppscopeConfigWithCustom(
        cribl=components.AppscopeConfigWithCustomCribl(
            transport=components.AppscopeTransport(
                tls=components.TLS(),
            ),
        ),
        custom=[
            components.AppscopeCustom(
                config=components.AppscopeConfig(
                    cribl=components.AppscopeConfigCribl(
                        transport=components.AppscopeTransport(
                            tls=components.TLS(),
                        ),
                    ),
                    event=components.Event(
                        enable=False,
                        format=components.AppscopeConfigFormat(
                            enhancefs=False,
                            maxeventpersec=486589,
                        ),
                        transport=components.AppscopeTransport(
                            tls=components.TLS(),
                        ),
                        type=components.AppscopeConfigType.NDJSON,
                        watch=[
                            components.Watch(
                                type='string',
                            ),
                        ],
                    ),
                    libscope=components.Libscope(
                        log=components.Log(
                            transport=components.AppscopeTransport(
                                tls=components.TLS(),
                            ),
                        ),
                    ),
                    metric=components.Metric(
                        enable=False,
                        format=components.AppscopeConfigSchemasFormat(),
                        transport=components.AppscopeTransport(
                            tls=components.TLS(),
                        ),
                        watch=[
                            'string',
                        ],
                    ),
                    payload=components.Payload(
                        dir='string',
                        enable=False,
                    ),
                    protocol=[
                        components.Protocol(
                            binary=False,
                            detect=False,
                            len=489382,
                            name='string',
                            payload=False,
                            regex='string',
                        ),
                    ],
                    tags=[
                        components.Tags(
                            key='<key>',
                            value='string',
                        ),
                    ],
                ),
            ),
        ],
        event=components.AppscopeConfigWithCustomEvent(
            enable=False,
            format=components.AppscopeConfigWithCustomFormat(
                enhancefs=False,
                maxeventpersec=638424,
            ),
            transport=components.AppscopeTransport(
                tls=components.TLS(),
            ),
            type=components.AppscopeConfigWithCustomType.NDJSON,
            watch=[
                components.AppscopeConfigWithCustomWatch(
                    type='string',
                ),
            ],
        ),
        libscope=components.AppscopeConfigWithCustomLibscope(
            log=components.AppscopeConfigWithCustomLog(
                transport=components.AppscopeTransport(
                    tls=components.TLS(),
                ),
            ),
        ),
        metric=components.AppscopeConfigWithCustomMetric(
            enable=False,
            format=components.AppscopeConfigWithCustomSchemasFormat(),
            transport=components.AppscopeTransport(
                tls=components.TLS(),
            ),
            watch=[
                'string',
            ],
        ),
        payload=components.AppscopeConfigWithCustomPayload(
            dir='string',
            enable=False,
        ),
        protocol=[
            components.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=859213,
                name='string',
                payload=False,
                regex='string',
            ),
        ],
        tags=[
            components.AppscopeConfigWithCustomTags(
                key='<key>',
                value='string',
            ),
        ],
    ),
    description='Inverse discrete benchmark',
    id='<ID>',
    lib=components.CriblLib.CUSTOM,
)

res = s.appscope_lib_entry.create(req)

if res.appscope_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.AppscopeLibEntry](../../models/components/appscopelibentry.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateAppscopeLibEntryResponse](../../models/operations/createappscopelibentryresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## delete

Delete AppscopeLibEntry

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## get

Get AppscopeLibEntry by ID

### Example Usage

```python
import cribl
from cribl.models import operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
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
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |

## update

Update AppscopeLibEntry

### Example Usage

```python
import cribl
from cribl.models import components, operations

s = cribl.Cribl(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.appscope_lib_entry.update(id='string', appscope_lib_entry=components.AppscopeLibEntry(
    config=components.AppscopeConfigWithCustom(
        cribl=components.AppscopeConfigWithCustomCribl(
            transport=components.AppscopeTransport(
                tls=components.TLS(),
            ),
        ),
        custom=[
            components.AppscopeCustom(
                config=components.AppscopeConfig(
                    cribl=components.AppscopeConfigCribl(
                        transport=components.AppscopeTransport(
                            tls=components.TLS(),
                        ),
                    ),
                    event=components.Event(
                        enable=False,
                        format=components.AppscopeConfigFormat(
                            enhancefs=False,
                            maxeventpersec=857478,
                        ),
                        transport=components.AppscopeTransport(
                            tls=components.TLS(),
                        ),
                        type=components.AppscopeConfigType.NDJSON,
                        watch=[
                            components.Watch(
                                type='string',
                            ),
                        ],
                    ),
                    libscope=components.Libscope(
                        log=components.Log(
                            transport=components.AppscopeTransport(
                                tls=components.TLS(),
                            ),
                        ),
                    ),
                    metric=components.Metric(
                        enable=False,
                        format=components.AppscopeConfigSchemasFormat(),
                        transport=components.AppscopeTransport(
                            tls=components.TLS(),
                        ),
                        watch=[
                            'string',
                        ],
                    ),
                    payload=components.Payload(
                        dir='string',
                        enable=False,
                    ),
                    protocol=[
                        components.Protocol(
                            binary=False,
                            detect=False,
                            len=24555,
                            name='string',
                            payload=False,
                            regex='string',
                        ),
                    ],
                    tags=[
                        components.Tags(
                            key='<key>',
                            value='string',
                        ),
                    ],
                ),
            ),
        ],
        event=components.AppscopeConfigWithCustomEvent(
            enable=False,
            format=components.AppscopeConfigWithCustomFormat(
                enhancefs=False,
                maxeventpersec=597129,
            ),
            transport=components.AppscopeTransport(
                tls=components.TLS(),
            ),
            type=components.AppscopeConfigWithCustomType.NDJSON,
            watch=[
                components.AppscopeConfigWithCustomWatch(
                    type='string',
                ),
            ],
        ),
        libscope=components.AppscopeConfigWithCustomLibscope(
            log=components.AppscopeConfigWithCustomLog(
                transport=components.AppscopeTransport(
                    tls=components.TLS(),
                ),
            ),
        ),
        metric=components.AppscopeConfigWithCustomMetric(
            enable=False,
            format=components.AppscopeConfigWithCustomSchemasFormat(),
            transport=components.AppscopeTransport(
                tls=components.TLS(),
            ),
            watch=[
                'string',
            ],
        ),
        payload=components.AppscopeConfigWithCustomPayload(
            dir='string',
            enable=False,
        ),
        protocol=[
            components.AppscopeConfigWithCustomProtocol(
                binary=False,
                detect=False,
                len=15652,
                name='string',
                payload=False,
                regex='string',
            ),
        ],
        tags=[
            components.AppscopeConfigWithCustomTags(
                key='<key>',
                value='string',
            ),
        ],
    ),
    description='Future-proofed next generation workforce',
    id='<ID>',
    lib=components.CriblLib.CRIBL,
))

if res.appscope_lib_entry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique ID                                                                            |
| `appscope_lib_entry`                                                                 | [Optional[components.AppscopeLibEntry]](../../models/components/appscopelibentry.md) | :heavy_minus_sign:                                                                   | AppscopeLibEntry object to be updated                                                |


### Response

**[operations.UpdateAppscopeLibEntryResponse](../../models/operations/updateappscopelibentryresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 401,500          | application/json |
| errors.SDKError  | 400-600          | */*              |
