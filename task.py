from dataclasses import dataclass, field
from typing import Callable

from messages import search_messages


@dataclass
class Task:
    query: str
    label_ids: list[str] = field(default_factory=list)
    actions: list[Callable] = field(default_factory=list)

    def execute(self, service):
        messages = search_messages(
            service, self.query, label_ids=self.label_ids
        )
        if not messages:
            return
        for action in self.actions:
            action(service, messages)
