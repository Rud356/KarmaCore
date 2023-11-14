from dataclasses import dataclass
from typing import Any


@dataclass
class Superuser:
    from_source: str
    extensions_superuser_parameters: dict[str, Any]


@dataclass(frozen=True)
class SuperusersConfig:
    superusers: tuple[Superuser]
