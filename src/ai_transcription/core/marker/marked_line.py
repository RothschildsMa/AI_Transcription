from dataclasses import dataclass, field
from typing import Set


@dataclass
class MarkedLine:
    text: str
    markers: Set[str] = field(default_factory=set)
