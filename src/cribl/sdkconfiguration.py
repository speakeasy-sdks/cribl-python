"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Callable, Union
from .utils.retries import RetryConfig
from .utils import utils
from cribl.models import components


SERVERS = [
    'https://logstream.{organizationID}.cribl.cloud/',
]
"""Contains the list of servers available to the SDK"""



@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[components.Security,Callable[[], components.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    server_defaults: List[Dict[str, str]] = field(default_factory=List)
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '1.0.0'
    gen_version: str = '2.225.2'
    user_agent: str = 'speakeasy-sdk/python 1.0.0 2.225.2 1.0.0 cribl'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], self.server_defaults[self.server_idx]
