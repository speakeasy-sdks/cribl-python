"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import searchterm as shared_searchterm
from ..shared import sortbyfield as shared_sortbyfield
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchConfig:
    datasets: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasets') }})
    has_send_operator: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasSendOperator') }})
    ordered_field_names: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orderedFieldNames') }})
    search_terms: List[shared_searchterm.SearchTerm] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searchTerms') }})
    suppress_event_marking: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suppressEventMarking') }})
    use_formatted_visualization: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useFormattedVisualization') }})
    sort_fields: Optional[List[shared_sortbyfield.SortByField]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortFields'), 'exclude': lambda f: f is None }})
    

