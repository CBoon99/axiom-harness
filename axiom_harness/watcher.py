"""Watcher — simple observer, lifecycle ARMED→COMPLETE (§43-44).

Records attempt→denied→trajectory as failed_policy events; never interprets.
"""
from enum import Enum

class Lifecycle(str, Enum):
    ARMED = "ARMED"
    STARTED = "STARTED"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    RESUMED = "RESUMED"
    STOPPING = "STOPPING"
    SEALED = "SEALED"
    COMPLETE = "COMPLETE"

class Watcher:
    def __init__(self, experiment_id: str):
        self.experiment_id = experiment_id
        self.lifecycle = Lifecycle.ARMED
        self.events: list = []

    def record(self, kind: str, payload: dict):
        self.events.append({"kind": kind, "payload": payload})

    # allowed transitions — no open jump, per lifecycle ARMED→STARTED→RUNNING→PAUSED→RESUMED→STOPPING→SEALED→COMPLETE
    _ALLOWED = {
        Lifecycle.ARMED: {Lifecycle.STARTED},
        Lifecycle.STARTED: {Lifecycle.RUNNING, Lifecycle.STOPPING},
        Lifecycle.RUNNING: {Lifecycle.PAUSED, Lifecycle.STOPPING},
        Lifecycle.PAUSED: {Lifecycle.RESUMED, Lifecycle.STOPPING},
        Lifecycle.RESUMED: {Lifecycle.RUNNING, Lifecycle.STOPPING},
        Lifecycle.STOPPING: {Lifecycle.SEALED},
        Lifecycle.SEALED: {Lifecycle.COMPLETE},
        Lifecycle.COMPLETE: set(),
    }

    def transition(self, to: Lifecycle):
        if to not in self._ALLOWED[self.lifecycle]:
            raise ValueError(f"illegal lifecycle {self.lifecycle} -> {to}")
        self.lifecycle = to
        self.record("lifecycle", {"to": to})
