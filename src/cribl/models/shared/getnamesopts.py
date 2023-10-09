"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import expression as shared_expression
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetNamesOpts:
    dim_key_filter: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimKeyFilter'), 'exclude': lambda f: f is None }})
    dim_value_filter: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimValueFilter'), 'exclude': lambda f: f is None }})
    earliest: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('earliest'), 'exclude': lambda f: f is None }})
    filter_expr: Optional[shared_expression.Expression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filterExpr'), 'exclude': lambda f: f is None }})
    max_values: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxValues'), 'exclude': lambda f: f is None }})
    metric_name_filter: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metricNameFilter'), 'exclude': lambda f: f is None }})
    

