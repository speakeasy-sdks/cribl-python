"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional



@dataclasses.dataclass
class SavedJobCollectionCollectorCollectorSpecificSettings:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollectionCollector:
    conf: SavedJobCollectionCollectorCollectorSpecificSettings = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conf') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of collector to run."""
    destructive: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destructive'), 'exclude': lambda f: f is None }})
    r"""If set to Yes, the collector will delete any files that it collects (where applicable)."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollectionInputMetadata:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Field name"""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollectionInputPreprocess:
    disabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled') }})
    r"""Enable Custom Command"""
    args: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('args'), 'exclude': lambda f: f is None }})
    r"""Arguments"""
    command: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('command'), 'exclude': lambda f: f is None }})
    r"""Command to feed the data through (via stdin) and process its output (stdout)"""
    


class SavedJobCollectionInputType(str, Enum):
    COLLECTION = 'collection'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollectionInput:
    breaker_rulesets: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('breakerRulesets'), 'exclude': lambda f: f is None }})
    r"""A list of event breaking rulesets that will be applied, in order, to the input data stream."""
    metadata: Optional[list[SavedJobCollectionInputMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""Fields to add to events from this input."""
    output: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output'), 'exclude': lambda f: f is None }})
    r"""Destination to send results to."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process results."""
    preprocess: Optional[SavedJobCollectionInputPreprocess] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preprocess'), 'exclude': lambda f: f is None }})
    send_to_routes: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sendToRoutes'), 'exclude': lambda f: f is None }})
    r"""If set to Yes, events will be sent to normal routing and event processing. Set to No if you want to select a specific Pipeline/Destination combination."""
    stale_channel_flush_ms: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('staleChannelFlushMs'), 'exclude': lambda f: f is None }})
    r"""The amount of time (in milliseconds) the Event Breaker will wait for new data to be sent to a specific channel, before flushing the data stream out, as-is, to the Pipelines."""
    throttle_rate_per_sec: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throttleRatePerSec'), 'exclude': lambda f: f is None }})
    r"""Rate (in bytes per second) to throttle while writing to an output. Also takes values with multiple-byte units, such as KB, MB, GB, etc. (E.g., 42 MB.) Default value of 0 specifies no throttling."""
    type: Optional[SavedJobCollectionInputType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SavedJobCollectionScheduleRunSettingsLogLevel(str, Enum):
    r"""Level at which to set task logging."""
    ERROR = 'error'
    WARN = 'warn'
    INFO = 'info'
    DEBUG = 'debug'
    SILLY = 'silly'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollectionScheduleRunSettings:
    earliest: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('earliest'), 'exclude': lambda f: f is None }})
    r"""Earliest time, for the given Range Timezone."""
    expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expression'), 'exclude': lambda f: f is None }})
    r"""A filter for tokens in the provided collect path and/or the events being collected"""
    job_timeout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time the job is allowed to run (e.g., 30, 45s or 15m). Units are seconds, if not specified. Enter 0 for unlimited time."""
    latest: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latest'), 'exclude': lambda f: f is None }})
    r"""Latest time, for the given Range Timezone."""
    log_level: Optional[SavedJobCollectionScheduleRunSettingsLogLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logLevel'), 'exclude': lambda f: f is None }})
    r"""Level at which to set task logging."""
    max_task_reschedule: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxTaskReschedule'), 'exclude': lambda f: f is None }})
    r"""Max number of times a task can be rescheduled."""
    max_task_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxTaskSize'), 'exclude': lambda f: f is None }})
    r"""Limits the bundle size for files above the Lower task bundle size. E.g., bundle five 2MB files into one 10MB task bundle. Files greater than this size will be assigned to individual tasks."""
    min_task_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minTaskSize'), 'exclude': lambda f: f is None }})
    r"""Limits the bundle size for small tasks. E.g., bundle five 200KB files into one 1M task."""
    mode: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    r"""Job run mode. Preview will either return up to N matching results, or will run until capture time T is reached. Discovery will gather the list of files to turn into streaming tasks, without running the data collection job. Full Run will run the collection job."""
    reschedule_dropped_tasks: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rescheduleDroppedTasks'), 'exclude': lambda f: f is None }})
    r"""Reschedule tasks that failed with non-fatal errors."""
    time_range_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeRangeType'), 'exclude': lambda f: f is None }})
    r"""Time range for scheduled job."""
    timestamp_timezone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampTimezone'), 'exclude': lambda f: f is None }})
    r"""Timezone to use for Earliest and Latest times (defaults to UTC)."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollectionSchedule:
    r"""Configuration for a scheduled job."""
    cron_schedule: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cronSchedule'), 'exclude': lambda f: f is None }})
    r"""A cron schedule on which to run this job."""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Determines whether or not this schedule is enabled."""
    max_concurrent_runs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxConcurrentRuns'), 'exclude': lambda f: f is None }})
    r"""The maximum number of instances that may be running of this scheduled job at any given time."""
    resume_missed: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resumeMissed'), 'exclude': lambda f: f is None }})
    run: Optional[SavedJobCollectionScheduleRunSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run'), 'exclude': lambda f: f is None }})
    skippable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skippable'), 'exclude': lambda f: f is None }})
    r"""Skippable jobs can be delayed, up to their next run time, if the system is hitting concurrency limits."""
    


class SavedJobCollectionJobType(str, Enum):
    r"""Job type."""
    COLLECTION = 'collection'
    EXECUTOR = 'executor'
    SCHEDULED_SEARCH = 'scheduledSearch'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SavedJobCollection:
    collector: SavedJobCollectionCollector = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collector') }})
    type: SavedJobCollectionJobType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Job type."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this Job."""
    input: Optional[SavedJobCollectionInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input'), 'exclude': lambda f: f is None }})
    remove_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removeFields'), 'exclude': lambda f: f is None }})
    r"""List of fields to remove from Discover results. Wildcards (e.g.: aws*) are allowed. This is useful when discovery returns sensitive fields that should not be exposed in the Jobs user interface."""
    resume_on_boot: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resumeOnBoot'), 'exclude': lambda f: f is None }})
    r"""Resumes the ad hoc job if a failure condition causes Stream to restart during job execution."""
    schedule: Optional[SavedJobCollectionSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    r"""Configuration for a scheduled job."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    ttl: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ttl'), 'exclude': lambda f: f is None }})
    r"""Time to keep the job's artifacts on disk after job completion. This also affects how long a job is listed in the Job Inspector."""
    worker_affinity: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workerAffinity'), 'exclude': lambda f: f is None }})
    r"""If enabled tasks are created and run by the same worker node."""
    

