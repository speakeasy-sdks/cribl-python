"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GitStatusResultFiles:
    index: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path') }})
    working_dir: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('working_dir') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GitStatusResultRenamed:
    from_: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from') }})
    to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GitStatusResult:
    ahead: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ahead') }})
    behind: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('behind') }})
    conflicted: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conflicted') }})
    created: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    current: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})
    deleted: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted') }})
    files: list[GitStatusResultFiles] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})
    modified: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modified') }})
    not_added: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('not_added') }})
    renamed: list[GitStatusResultRenamed] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('renamed') }})
    staged: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('staged') }})
    tracking: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking') }})
    

