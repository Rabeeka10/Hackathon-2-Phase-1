"""Todo model definition.

This module defines the Todo dataclass used throughout the application.
The model is designed to be simple, type-safe, and compatible with
future database-backed implementations in Phase II.
"""

from dataclasses import dataclass


@dataclass
class Todo:
    """Represents a single todo item.

    Attributes:
        id: Unique positive integer, auto-assigned, immutable after creation.
        title: Non-empty string, required.
        completed: Boolean status (True = complete, False = incomplete).
        description: Optional string, can be empty.
    """

    id: int
    title: str
    completed: bool = False
    description: str = ""
