# saved_jobs

### Available Operations

* [create](#create) - Create SavedJob
* [get](#get) - Get a list of SavedJob objects

## create

Create SavedJob

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SavedJobCollection(
    collector=shared.SavedJobCollectionCollector(
        conf=shared.SavedJobCollectionCollectorCollectorSpecificSettings(),
        destructive=False,
        type='vel',
    ),
    environment='amet',
    id='bbca4922-7c42-4c22-8553-50495c5dbb3c',
    input=shared.SavedJobCollectionInput(
        breaker_rulesets=[
            'reprehenderit',
            'quo',
        ],
        metadata=[
            shared.SavedJobCollectionInputMetadata(
                name='Ricky Moore DVM',
                value='atque',
            ),
        ],
        output='dolorum',
        pipeline='similique',
        preprocess=shared.SavedJobCollectionInputPreprocess(
            args=[
                'enim',
            ],
            command='quam',
            disabled=False,
        ),
        send_to_routes=False,
        stale_channel_flush_ms=828001,
        throttle_rate_per_sec='temporibus',
        type=shared.SavedJobCollectionInputType.COLLECTION,
    ),
    remove_fields=[
        'quasi',
        'sint',
        'inventore',
        'fugit',
    ],
    resume_on_boot=False,
    schedule=shared.SavedJobCollectionSchedule(
        cron_schedule='earum',
        enabled=False,
        max_concurrent_runs=697382,
        resume_missed='at',
        run=shared.SavedJobCollectionScheduleRunSettings(
            earliest=895349,
            expression='eum',
            job_timeout='non',
            latest=724043,
            log_level=shared.SavedJobCollectionScheduleRunSettingsLogLevel.SILLY,
            max_task_reschedule=784353,
            max_task_size='impedit',
            min_task_size='veniam',
            mode='magnam',
            reschedule_dropped_tasks=False,
            time_range_type='iure',
            timestamp_timezone='natus',
        ),
        skippable=False,
    ),
    streamtags=[
        'quaerat',
        'aut',
        'architecto',
        'quis',
    ],
    ttl='possimus',
    type=shared.SavedJobCollectionJobType.SCHEDULED_SEARCH,
    worker_affinity=False,
)

res = s.saved_jobs.create(req)

if res.saved_jobs is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [Any](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateSavedJobsResponse](../../models/operations/createsavedjobsresponse.md)**


## get

Get a list of SavedJob objects

### Example Usage

```python
import cribl
from cribl.models import shared

s = cribl.Cribl(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.saved_jobs.get()

if res.saved_jobs is not None:
    # handle response
```


### Response

**[operations.GetSavedJobsResponse](../../models/operations/getsavedjobsresponse.md)**

