"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class PipelineFunctionConfFunctionSpecificConfigs:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PipelineFunctionConf:
    conf: PipelineFunctionConfFunctionSpecificConfigs = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conf') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Function ID"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Simple description of this step"""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    r"""If true, data will not be pushed through this function"""
    filter: Optional[str] = dataclasses.field(default='true', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})
    r"""Filter that selects data to be fed through this function"""
    final: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('final'), 'exclude': lambda f: f is None }})
    r"""If true, stops the results of this function from being passed to the downstream functions"""
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupId'), 'exclude': lambda f: f is None }})
    r"""Group ID"""
    

