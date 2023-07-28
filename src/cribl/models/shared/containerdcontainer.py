"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import containerdmount as shared_containerdmount
from ..shared import containerdroot as shared_containerdroot
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContainerdContainer:
    mounts: list[shared_containerdmount.ContainerdMount] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mounts') }})
    root: shared_containerdroot.ContainerdRoot = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('root') }})
    
