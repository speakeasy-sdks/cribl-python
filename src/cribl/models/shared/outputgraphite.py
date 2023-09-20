"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from cribl import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class OutputGraphiteBackpressureBehavior(str, Enum):
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    QUEUE = 'queue'
    DROP = 'drop'
    BLOCK = 'block'

class OutputGraphiteCompression(str, Enum):
    r"""Codec to use to compress the persisted data."""
    NONE = 'none'
    GZIP = 'gzip'



@dataclasses.dataclass
class OutputGraphitePqControls:
    pass

class OutputGraphiteQueueFullBehavior(str, Enum):
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    BLOCK = 'block'
    DROP = 'drop'

class OutputGraphiteDestinationProtocol(str, Enum):
    r"""Protocol to use when communicating with the destination."""
    TCP = 'tcp'

class OutputGraphiteType(str, Enum):
    GRAPHITE = 'graphite'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OutputGraphite:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The hostname of the destination."""
    connection_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for the connection to establish before retrying"""
    environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    flush_period_sec: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flushPeriodSec'), 'exclude': lambda f: f is None }})
    r"""Used when Protocol is TCP, to specify how often buffers should be flushed resulting in records sent to the destination."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique ID for this output"""
    mtu: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mtu'), 'exclude': lambda f: f is None }})
    r"""Used when Protocol is UDP, to specify the maximum size of packets sent to the destination. Also known as the MTU for the network path to the destination system."""
    on_backpressure: Optional[OutputGraphiteBackpressureBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block, drop, or queue events when all receivers are exerting backpressure."""
    pipeline: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline'), 'exclude': lambda f: f is None }})
    r"""Pipeline to process data before sending out to this output."""
    port: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Destination port."""
    pq_compress: Optional[OutputGraphiteCompression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqCompress'), 'exclude': lambda f: f is None }})
    r"""Codec to use to compress the persisted data."""
    pq_controls: Optional[OutputGraphitePqControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqControls'), 'exclude': lambda f: f is None }})
    pq_max_file_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxFileSize'), 'exclude': lambda f: f is None }})
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)."""
    pq_max_size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqMaxSize'), 'exclude': lambda f: f is None }})
    r"""The maximum amount of disk space the queue is allowed to consume. Once reached, the system stops queueing and applies the fallback Queue-full behavior. Enter a numeral with units of KB, MB, etc."""
    pq_on_backpressure: Optional[OutputGraphiteQueueFullBehavior] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqOnBackpressure'), 'exclude': lambda f: f is None }})
    r"""Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqPath'), 'exclude': lambda f: f is None }})
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_strict_ordering: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pqStrictOrdering'), 'exclude': lambda f: f is None }})
    r"""Toggle this off to forward new events to receiver(s) before queue is flushed. Otherwise, default drain behavior is FIFO (first in, first out)."""
    protocol: Optional[OutputGraphiteDestinationProtocol] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protocol'), 'exclude': lambda f: f is None }})
    r"""Protocol to use when communicating with the destination."""
    streamtags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamtags'), 'exclude': lambda f: f is None }})
    r"""Add tags for filtering and grouping in @{product}."""
    system_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemFields'), 'exclude': lambda f: f is None }})
    r"""Set of fields to automatically add to events using this output. E.g.: cribl_pipe, c*. Wildcards supported."""
    throttle_rate_per_sec: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('throttleRatePerSec'), 'exclude': lambda f: f is None }})
    r"""Rate (in bytes per second) to throttle while writing to an output. Also takes values with multiple-byte units, such as KB, MB, GB, etc. (E.g., 42 MB.) Default value of 0 specifies no throttling."""
    type: Optional[OutputGraphiteType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    write_timeout: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('writeTimeout'), 'exclude': lambda f: f is None }})
    r"""Amount of time (milliseconds) to wait for a write to complete before assuming connection is dead"""
    

