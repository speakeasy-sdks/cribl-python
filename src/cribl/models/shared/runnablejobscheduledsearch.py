"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class RunnableJobScheduledSearchScheduleRunSettingsLogLevel(str, Enum):
    r"""Level at which to set task logging."""
    ERROR = 'error'
    WARN = 'warn'
    INFO = 'info'
    DEBUG = 'debug'
    SILLY = 'silly'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RunnableJobScheduledSearchScheduleRunSettings:
    earliest: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('earliest'), 'exclude': lambda f: f is None }})
    r"""Earliest time, for the given Range Timezone."""
    expression: Optional[str] = dataclasses.field(default='true', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expression'), 'exclude': lambda f: f is None }})
    r"""A filter for tokens in the provided collect path and/or the events being collected"""
    job_timeout: Optional[str] = dataclasses.field(default='0', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobTimeout'), 'exclude': lambda f: f is None }})
    r"""Maximum time the job is allowed to run (e.g., 30, 45s or 15m). Units are seconds, if not specified. Enter 0 for unlimited time."""
    latest: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latest'), 'exclude': lambda f: f is None }})
    r"""Latest time, for the given Range Timezone."""
    log_level: Optional[RunnableJobScheduledSearchScheduleRunSettingsLogLevel] = dataclasses.field(default=RunnableJobScheduledSearchScheduleRunSettingsLogLevel.INFO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logLevel'), 'exclude': lambda f: f is None }})
    r"""Level at which to set task logging."""
    max_task_reschedule: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxTaskReschedule'), 'exclude': lambda f: f is None }})
    r"""Max number of times a task can be rescheduled."""
    max_task_size: Optional[str] = dataclasses.field(default='10MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxTaskSize'), 'exclude': lambda f: f is None }})
    r"""Limits the bundle size for files above the Lower task bundle size. E.g., bundle five 2MB files into one 10MB task bundle. Files greater than this size will be assigned to individual tasks."""
    min_task_size: Optional[str] = dataclasses.field(default='1MB', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minTaskSize'), 'exclude': lambda f: f is None }})
    r"""Limits the bundle size for small tasks. E.g., bundle five 200KB files into one 1M task."""
    mode: Optional[str] = dataclasses.field(default='list', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    r"""Job run mode. Preview will either return up to N matching results, or will run until capture time T is reached. Discovery will gather the list of files to turn into streaming tasks, without running the data collection job. Full Run will run the collection job."""
    reschedule_dropped_tasks: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rescheduleDroppedTasks'), 'exclude': lambda f: f is None }})
    r"""Reschedule tasks that failed with non-fatal errors."""
    time_range_type: Optional[str] = dataclasses.field(default='relative', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeRangeType'), 'exclude': lambda f: f is None }})
    r"""Time range for scheduled job."""
    timestamp_timezone: Optional[str] = dataclasses.field(default='UTC', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestampTimezone'), 'exclude': lambda f: f is None }})
    r"""Timezone to use for Earliest and Latest times (defaults to UTC)."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RunnableJobScheduledSearchSchedule:
    r"""Configuration for a scheduled job."""
    cron_schedule: Optional[str] = dataclasses.field(default='*/5 * * * *', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cronSchedule'), 'exclude': lambda f: f is None }})
    r"""A cron schedule on which to run this job."""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Determines whether or not this schedule is enabled."""
    max_concurrent_runs: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxConcurrentRuns'), 'exclude': lambda f: f is None }})
    r"""The maximum number of instances that may be running of this scheduled job at any given time."""
    resume_missed: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resumeMissed'), 'exclude': lambda f: f is None }})
    run: Optional[RunnableJobScheduledSearchScheduleRunSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run'), 'exclude': lambda f: f is None }})
    skippable: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skippable'), 'exclude': lambda f: f is None }})
    r"""Skippable jobs can be delayed, up to their next run time, if the system is hitting concurrency limits."""
    


class RunnableJobScheduledSearchJobType(str, Enum):
    r"""Job type."""
    COLLECTION = 'collection'
    EXECUTOR = 'executor'
    SCHEDULED_SEARCH = 'scheduledSearch'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RunnableJobScheduledSearch:
    saved_query_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('savedQueryId') }})
    r"""Identifies which search query to run"""
    type: RunnableJobScheduledSearchJobType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Job type."""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this Job."""
    remove_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('removeFields'), 'exclude': lambda f: f is None }})
    r"""List of fields to remove from Discover results. Wildcards (e.g.: aws*) are allowed. This is useful when discovery returns sensitive fields that should not be exposed in the Jobs user interface."""
    resume_on_boot: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resumeOnBoot'), 'exclude': lambda f: f is None }})
    r"""Resumes the ad hoc job if a failure condition causes Stream to restart during job execution."""
    schedule: Optional[RunnableJobScheduledSearchSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    r"""Configuration for a scheduled job."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    ttl: Optional[str] = dataclasses.field(default='4h', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ttl'), 'exclude': lambda f: f is None }})
    r"""Time to keep the job's artifacts on disk after job completion. This also affects how long a job is listed in the Job Inspector."""
    

