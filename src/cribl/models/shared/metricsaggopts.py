"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import aggregationmgroptions as shared_aggregationmgroptions
from ..shared import metricsstore as shared_metricsstore
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MetricsAggOpts:
    r"""MetricsAggOpts object"""
    aggs: shared_aggregationmgroptions.AggregationMgrOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aggs') }})
    always_bounds: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alwaysBounds'), 'exclude': lambda f: f is None }})
    metrics: Optional[shared_metricsstore.MetricsStore] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics'), 'exclude': lambda f: f is None }})
    where: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('where'), 'exclude': lambda f: f is None }})
    

