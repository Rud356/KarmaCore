import asyncio
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

PositiveChange = TypeVar("PositiveChange")
NegativeChange = TypeVar("NegativeChange")
Restriction = TypeVar("Restriction")


class ExtensionBase(ABC, Generic[PositiveChange, NegativeChange, Restriction]):
    def __init__(self):
        self.positive_changes_queue: asyncio.Queue[PositiveChange] = asyncio.Queue()
        self.negative_changes_queue: asyncio.Queue[NegativeChange] = asyncio.Queue()
        self.restriction_queue: asyncio.Queue[Restriction] = asyncio.Queue()

    @abstractmethod
    async def triggered_positive_change(self) -> float:
        """
        Called when users karma level is being changed by other user positively.

        :return: amount that karma been changed.
        """
        pass

    @abstractmethod
    async def triggered_negative_change(self) -> float:
        """
        Called when users karma level is being changed by other user negatively.

        :return: amount that karma been changed.
        """
        pass

    @abstractmethod
    async def trigger_restriction(self) -> bool:
        """
        Executes restriction process if user fell below threshold and restrictions in source are enabled.

        :return: has user been restricted.
        """

    @abstractmethod
    async def start(self) -> asyncio.Task:
        """
        Creates a task that waits for some triggers.

        :return: task group for two subtasks. First fetches messages and checks if they had triggers for changes. Second
        executes changes and restrictions in case user crossed threshold, and restrictions are enabled.
        """