"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .axis import Axis
from .chartseries import ChartSeries
from .legend import Legend
from .settings import Settings
from .singlevalue import SingleValue
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChartConfigAxis:
    x_axis: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('xAxis'), 'exclude': lambda f: f is None }})
    y_axis: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('yAxis'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChartConfig:
    single_value: SingleValue = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('singleValue') }})
    axis: Optional[ChartConfigAxis] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('axis'), 'exclude': lambda f: f is None }})
    legend: Optional[Legend] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legend'), 'exclude': lambda f: f is None }})
    series: Optional[List[ChartSeries]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('series'), 'exclude': lambda f: f is None }})
    settings: Optional[Settings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settings'), 'exclude': lambda f: f is None }})
    x_axis: Optional[Axis] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('xAxis'), 'exclude': lambda f: f is None }})
    

