"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Files:
    index: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path') }})
    working_dir: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('working_dir') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Renamed:
    from_: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from') }})
    to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GitStatusResult:
    ahead: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ahead') }})
    behind: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('behind') }})
    conflicted: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conflicted') }})
    created: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    current: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})
    deleted: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted') }})
    files: List[Files] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})
    modified: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modified') }})
    not_added: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('not_added') }})
    renamed: List[Renamed] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('renamed') }})
    staged: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('staged') }})
    tracking: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking') }})
    
