# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Literal


EventContentTypes = Literal["application/json", "application/octet-stream"]


@dataclass(frozen=True, kw_only=True)
class NewEvent:
    """
    Encapsulates event data to be recorded in EventStoreDB.
    """

    type: str
    data: bytes
    metadata: bytes
    contentType: EventContentTypes = field(default="application/octet-stream")


@dataclass(frozen=True, kw_only=True)
class RecordedEvent(NewEvent):
    """
    Encapsulates event data that has been recorded in EventStoreDB.
    """

    stream_name: str
    stream_position: int
    commit_position: int

