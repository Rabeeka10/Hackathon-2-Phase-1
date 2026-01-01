"""In-memory storage for todo items.

This module provides the TodoStore class that manages all todo items
in memory. It handles ID generation, CRUD operations, and maintains
the invariant that IDs are never reused after deletion.
"""

from src.models import Todo


class TodoStore:
    """In-memory collection that manages Todo entities.

    The store maintains a dictionary mapping IDs to Todo objects and
    tracks the next available ID. IDs are monotonically increasing
    and never reused, even after deletion.

    Attributes:
        _todos: Dictionary mapping ID to Todo entity.
        _next_id: Next available ID for new todos (starts at 1).
    """

    def __init__(self) -> None:
        """Initialize an empty todo store."""
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def add(self, title: str, description: str = "") -> Todo:
        """Create a new todo with auto-assigned ID.

        Args:
            title: The title for the new todo (must be non-empty).
            description: Optional description for the todo.

        Returns:
            The newly created Todo with assigned ID.
        """
        todo = Todo(
            id=self._next_id,
            title=title,
            completed=False,
            description=description,
        )
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def get(self, todo_id: int) -> Todo | None:
        """Retrieve a single todo by ID.

        Args:
            todo_id: The ID of the todo to retrieve.

        Returns:
            The Todo if found, None otherwise.
        """
        return self._todos.get(todo_id)

    def get_all(self) -> list[Todo]:
        """Retrieve all todos in insertion order.

        Returns:
            List of all Todo entities, ordered by insertion.
        """
        return list(self._todos.values())

    def update(
        self,
        todo_id: int,
        title: str | None = None,
        description: str | None = None,
    ) -> Todo | None:
        """Update an existing todo's fields.

        Args:
            todo_id: The ID of the todo to update.
            title: New title (None = keep existing).
            description: New description (None = keep existing).

        Returns:
            The updated Todo if found, None otherwise.
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            return None

        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description

        return todo

    def delete(self, todo_id: int) -> bool:
        """Remove a todo by ID.

        The ID is never reused after deletion.

        Args:
            todo_id: The ID of the todo to delete.

        Returns:
            True if the todo was deleted, False if not found.
        """
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False

    def set_completed(self, todo_id: int, completed: bool) -> Todo | None:
        """Set the completion status of a todo.

        Args:
            todo_id: The ID of the todo to update.
            completed: The new completion status.

        Returns:
            The updated Todo if found, None otherwise.
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            return None

        todo.completed = completed
        return todo
