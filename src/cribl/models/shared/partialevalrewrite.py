"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import partialevalfieldfilter as shared_partialevalfieldfilter
from cribl import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PartialEvalRewrite:
    field_filter: shared_partialevalfieldfilter.PartialEvalFieldFilter = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fieldFilter') }})
    null_obj: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nullObj') }})
    

