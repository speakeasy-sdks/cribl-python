"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .expressionoptions import ExpressionOptions
from .map import Map
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Expression:
    cache: Map = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cache') }})
    declared_variables: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('declaredVariables') }})
    is_safe: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSafe') }})
    max_cache: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('MAX_CACHE') }})
    modified_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedExpression') }})
    opt: ExpressionOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opt') }})
    original_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('originalExpression') }})
    partial_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partialExpression') }})
    referenced_cribl_export: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('referencedCriblExport') }})
    replace_identifiers_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replaceIdentifiersExpression') }})
    replace_literal_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replaceLiteralExpression') }})
    
