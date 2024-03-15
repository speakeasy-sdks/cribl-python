"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RoutesRouteInput:
    UNSET='__SPEAKEASY_UNSET__'
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    pipeline: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline') }})
    r"""Pipeline to send the matching data to"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Short description of this Route"""
    disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is None }})
    r"""Whether this routing rule is disabled"""
    enable_output_expression: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableOutputExpression'), 'exclude': lambda f: f is None }})
    r"""If toggled to Yes, you can use a JavaScript expression that evaluates to the name of the Output below"""
    filter_: Optional[str] = dataclasses.field(default='true', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})
    r"""Expression (JS) to select data to route"""
    final: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('final'), 'exclude': lambda f: f is None }})
    r"""Flag to control whether the event gets consumed by this Route (Final), or cloned into it"""
    output: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output'), 'exclude': lambda f: f is None }})
    output_expression: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outputExpression'), 'exclude': lambda f: f is None }})
    

