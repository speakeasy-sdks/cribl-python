"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import edgeheartbeatmetricsmode as shared_edgeheartbeatmetricsmode
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LimitsSamples:
    max_size: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxSize') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Limits:
    cpu_profile_ttl: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cpuProfileTTL') }})
    enable_metrics_persistence: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableMetricsPersistence') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    metrics_directory: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsDirectory') }})
    metrics_fields_blacklist: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsFieldsBlacklist') }})
    metrics_gc_period: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsGCPeriod') }})
    metrics_never_drop_list: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsNeverDropList') }})
    metrics_worker_id_blacklist: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsWorkerIdBlacklist') }})
    min_free_space: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minFreeSpace') }})
    samples: LimitsSamples = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('samples') }})
    edge_metrics_custom_expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('edgeMetricsCustomExpression'), 'exclude': lambda f: f is None }})
    edge_metrics_mode: Optional[shared_edgeheartbeatmetricsmode.EdgeHeartbeatMetricsMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('edgeMetricsMode'), 'exclude': lambda f: f is None }})
    events_metadata_sources: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventsMetadataSources'), 'exclude': lambda f: f is None }})
    metrics_max_cardinality: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsMaxCardinality'), 'exclude': lambda f: f is None }})
    metrics_max_disk_space: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricsMaxDiskSpace'), 'exclude': lambda f: f is None }})
    

