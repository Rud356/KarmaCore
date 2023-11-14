from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ExtConfiguration:
    total_extensions_count: int
    enabled_extensions: list[dict[str, Any]]
    all_extensions: list[dict[str, Any]]
