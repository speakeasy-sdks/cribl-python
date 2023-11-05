"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DistributedSummaryGroups:
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    destinations: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinations') }})
    pipelines: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipelines') }})
    routes: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routes') }})
    sources: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sources') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DistributedSummaryWorkers:
    alive: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alive') }})
    conf_versions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confVersions') }})
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    groups: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groups') }})
    software_versions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('softwareVersions') }})
    unhealthy: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unhealthy') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DistributedSummary:
    groups: DistributedSummaryGroups = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groups') }})
    workers: DistributedSummaryWorkers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workers') }})
    

