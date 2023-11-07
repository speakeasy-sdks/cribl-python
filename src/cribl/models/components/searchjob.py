"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .chartconfig import ChartConfig
from .cputimemetric import CPUTimeMetric
from .datatypeoverrides import DatatypeOverrides
from .searchconfig import SearchConfig
from .searchjoberrorstateconfig import SearchJobErrorStateConfig
from .searchjobstatus import SearchJobStatus
from .searchjobtype import SearchJobType
from .searchparameter import SearchParameter
from .tableviewsettings import TableViewSettings
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompatibilityChecks:
    datatypes: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datatypes'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchJob:
    group: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    search_config: SearchConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searchConfig') }})
    status: SearchJobStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    time_created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeCreated') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    chart_config: Optional[ChartConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chartConfig'), 'exclude': lambda f: f is None }})
    compatibility_checks: Optional[CompatibilityChecks] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compatibilityChecks'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})
    cpu_metrics: Optional[CPUTimeMetric] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cpuMetrics'), 'exclude': lambda f: f is None }})
    datatype_overrides: Optional[DatatypeOverrides] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datatypeOverrides'), 'exclude': lambda f: f is None }})
    earliest_epoch: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('earliestEpoch'), 'exclude': lambda f: f is None }})
    error_state_config: Optional[SearchJobErrorStateConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorStateConfig'), 'exclude': lambda f: f is None }})
    latest_epoch: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestEpoch'), 'exclude': lambda f: f is None }})
    num_events_after: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numEventsAfter'), 'exclude': lambda f: f is None }})
    num_events_before: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numEventsBefore'), 'exclude': lambda f: f is None }})
    sample_rate: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sampleRate'), 'exclude': lambda f: f is None }})
    search_parameter_declarations: Optional[List[SearchParameter]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searchParameterDeclarations'), 'exclude': lambda f: f is None }})
    search_parameter_values: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searchParameterValues'), 'exclude': lambda f: f is None }})
    table_config: Optional[TableViewSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tableConfig'), 'exclude': lambda f: f is None }})
    target_event_time: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targetEventTime'), 'exclude': lambda f: f is None }})
    time_completed: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeCompleted'), 'exclude': lambda f: f is None }})
    time_started: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeStarted'), 'exclude': lambda f: f is None }})
    type: Optional[SearchJobType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    
