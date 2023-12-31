"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MappingRulesetConf:
    functions: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('functions'), 'exclude': lambda f: f is None }})
    r"""List of functions to pass data through"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MappingRuleset:
    r"""New MappingRuleset object"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Ruleset ID"""
    active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active'), 'exclude': lambda f: f is None }})
    conf: Optional[MappingRulesetConf] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conf'), 'exclude': lambda f: f is None }})
    

