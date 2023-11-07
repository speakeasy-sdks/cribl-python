"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .gitfile import GitFile
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Dict, List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GitFilesResponse:
    commit_message: Dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commitMessage') }})
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    items: List[GitFile] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    
