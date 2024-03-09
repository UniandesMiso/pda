from uuid import UUID
from datetime import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

from properties.seedwork.application.commands import Command, execute_command
from properties.seedwork.domain.events import DomainEvent


class Coordinator(ABC):
    id: UUID

    @abstractmethod
    def start(self): ...

    @abstractmethod
    def finish(self): ...

    @abstractmethod
    def initialize_steps(self): ...

    @abstractmethod
    def save_log(self, message): ...

    @abstractmethod
    def process_event(self, event: DomainEvent): ...

    @abstractmethod
    def build_command(self, event: DomainEvent, command_type: type) -> Command: ...

    @abstractmethod
    def send_command(self, event: DomainEvent, command_type: type):
        command = self.build_command(event, command_type)
        execute_command(command)


class Step:
    id: UUID
    index: int
    executed_at: datetime


@dataclass
class Start(Step):
    index: int = 0


@dataclass
class End(Step): ...


@dataclass
class Transaction(Step):
    command: Command
    event: DomainEvent
    error: DomainEvent
    compensation: Command
    is_successful: bool


class OrchestrationCoordinator(Coordinator):
    index: int
    steps: list[Step]

    def is_first(self, index):
        return index == 1

    def is_last(self, index):
        return len(self.steps) - 1 == index
    
    def has_to_finish(self, event, i, step):
        return (
            (self.is_first(i) and isinstance(event, step.error)) or
            (self.is_last(i) and not isinstance(event, step.error))
        )

    def get_step_by_event(self, event: DomainEvent):
        for i, step in enumerate(self.steps):
            if not isinstance(step, Transaction): continue
            if isinstance(event, step.event): return i, step
        return None
    
    def process_event(self, event: DomainEvent):
        i, step = self.get_step_by_event(event)
        if self.has_to_finish(event, i, step):
            self.finish()
        elif isinstance(event, step.error):
            self.send_command(event, self.steps[i - 1].compensation)
        elif isinstance(event, step.event):
            self.send_command(event, self.steps[i + 1].command)
