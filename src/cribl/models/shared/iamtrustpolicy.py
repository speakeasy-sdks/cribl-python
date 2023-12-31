"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class IAMTrustPolicyStatementConditionStringEquals:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IAMTrustPolicyStatementCondition:
    string_equals: Optional[IAMTrustPolicyStatementConditionStringEquals] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StringEquals'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IAMTrustPolicyStatementPrincipal:
    aws: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AWS') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IAMTrustPolicyStatement:
    action: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Action') }})
    effect: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Effect') }})
    principal: IAMTrustPolicyStatementPrincipal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Principal') }})
    condition: Optional[IAMTrustPolicyStatementCondition] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Condition'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IAMTrustPolicy:
    statement: list[IAMTrustPolicyStatement] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Statement') }})
    version: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Version') }})
    

