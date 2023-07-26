"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import databaseconnectiontype as shared_databaseconnectiontype
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DatabaseConnectionConfig:
    r"""New DatabaseConnectionConfig object"""
    auth_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authType') }})
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    config_obj: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configObj'), 'exclude': lambda f: f is None }})
    connection_string: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionString'), 'exclude': lambda f: f is None }})
    connection_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    database_type: Optional[shared_databaseconnectiontype.DatabaseConnectionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databaseType'), 'exclude': lambda f: f is None }})
    request_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestTimeout'), 'exclude': lambda f: f is None }})
    tags: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    

