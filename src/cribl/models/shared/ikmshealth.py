"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import ikmshealthtest as shared_ikmshealthtest
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IKMSHealth:
    auth: shared_ikmshealthtest.IKMSHealthTest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth') }})
    connection: shared_ikmshealthtest.IKMSHealthTest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection') }})
    system: shared_ikmshealthtest.IKMSHealthTest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('system') }})
    

