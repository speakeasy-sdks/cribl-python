"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpgradeMasterRequestPackages:
    package_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('packageUrl') }})
    r"""Package HTTP URL or local path."""
    package_hash_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('packageHashUrl'), 'exclude': lambda f: f is None }})
    r"""Package's MD5 or SHA256 hash HTTP URL or local path."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpgradeMasterRequest:
    r"""upgradeMaster object"""
    packages: Optional[list[UpgradeMasterRequestPackages]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('packages'), 'exclude': lambda f: f is None }})
    r"""Provide your own URLs or local paths for platform-specific Cribl packages."""
    

