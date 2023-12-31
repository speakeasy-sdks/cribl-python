"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dockergraphdriver as shared_dockergraphdriver
from ..shared import dockermount as shared_dockermount
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DockerInfo:
    config: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Config'), 'exclude': lambda f: f is None }})
    graph_driver: Optional[shared_dockergraphdriver.DockerGraphDriver] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('GraphDriver'), 'exclude': lambda f: f is None }})
    log_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('LogPath'), 'exclude': lambda f: f is None }})
    mounts: Optional[list[shared_dockermount.DockerMount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Mounts'), 'exclude': lambda f: f is None }})
    network_settings: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NetworkSettings'), 'exclude': lambda f: f is None }})
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Path'), 'exclude': lambda f: f is None }})
    state: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('State'), 'exclude': lambda f: f is None }})
    stats: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Stats'), 'exclude': lambda f: f is None }})
    

