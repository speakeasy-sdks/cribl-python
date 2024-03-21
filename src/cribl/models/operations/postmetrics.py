"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import metricsinfo as components_metricsinfo
from typing import Optional


@dataclasses.dataclass
class PostMetricsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    metrics_info: Optional[components_metricsinfo.MetricsInfo] = dataclasses.field(default=None)
    r"""a list of MetricNameInfo objects"""
    

