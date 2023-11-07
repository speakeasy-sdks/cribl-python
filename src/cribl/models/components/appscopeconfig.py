"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .appscopetransport import AppscopeTransport
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppscopeConfigCribl:
    authtoken: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authtoken'), 'exclude': lambda f: f is None }})
    enable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable'), 'exclude': lambda f: f is None }})
    transport: Optional[AppscopeTransport] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transport'), 'exclude': lambda f: f is None }})
    use_scope_source_transport: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useScopeSourceTransport'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppscopeConfigFormat:
    enhancefs: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enhancefs') }})
    maxeventpersec: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxeventpersec') }})
    


class AppscopeConfigType(str, Enum):
    NDJSON = 'ndjson'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Watch:
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    allowbinary: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowbinary'), 'exclude': lambda f: f is None }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    headers: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headers'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Event:
    enable: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable') }})
    format: AppscopeConfigFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    transport: AppscopeTransport = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transport') }})
    type: AppscopeConfigType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    watch: List[Watch] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watch') }})
    


class Level(str, Enum):
    DEBUG = 'debug'
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Log:
    level: Optional[Level] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('level'), 'exclude': lambda f: f is None }})
    transport: Optional[AppscopeTransport] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transport'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Libscope:
    commanddir: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commanddir'), 'exclude': lambda f: f is None }})
    configevent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configevent'), 'exclude': lambda f: f is None }})
    log: Optional[Log] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('log'), 'exclude': lambda f: f is None }})
    summaryperiod: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summaryperiod'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppscopeConfigSchemasFormat:
    statsdmaxlen: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statsdmaxlen'), 'exclude': lambda f: f is None }})
    statsdprefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statsdprefix'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    verbosity: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verbosity'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Metric:
    enable: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable') }})
    format: AppscopeConfigSchemasFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    transport: AppscopeTransport = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transport') }})
    watch: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('watch') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Payload:
    dir: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dir') }})
    enable: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Protocol:
    binary: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('binary') }})
    detect: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detect') }})
    len: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('len') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    payload: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload') }})
    regex: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('regex') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tags:
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppscopeConfig:
    cribl: Optional[AppscopeConfigCribl] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cribl'), 'exclude': lambda f: f is None }})
    event: Optional[Event] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event'), 'exclude': lambda f: f is None }})
    libscope: Optional[Libscope] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('libscope'), 'exclude': lambda f: f is None }})
    metric: Optional[Metric] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metric'), 'exclude': lambda f: f is None }})
    payload: Optional[Payload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload'), 'exclude': lambda f: f is None }})
    protocol: Optional[List[Protocol]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protocol'), 'exclude': lambda f: f is None }})
    tags: Optional[List[Tags]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    
