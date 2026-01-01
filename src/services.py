"""Business logic for todo operations.

This module contains pure business logic functions that operate on the
TodoStore. These functions are decoupled from I/O and can be called
from any interface (CLI, API, etc.).
"""

from src.models import Todo
from src.store import TodoStore


def create_todo(store: TodoStore, title: str, description: str = "") -> Todo:
    """Create a new todo item.

    Args:
        store: The TodoStore instance to add the todo to.
        title: The title for the new todo (must be non-empty).
        description: Optional description for the todo.

    Returns:
        The newly created Todo.

    Raises:
        ValueError: If title is empty or whitespace-only.
    """
    title = title.strip()
    if not title:
        raise ValueError("Title cannot be empty")

    return store.add(title, description.strip())


def list_todos(store: TodoStore) -> list[Todo]:
    """Get all todos from the store.

    Args:
        store: The TodoStore instance to query.

    Returns:
        List of all todos in insertion order.
    """
    return store.get_all()


def get_todo(store: TodoStore, todo_id: int) -> Todo | None:
    """Get a single todo by ID.

    Args:
        store: The TodoStore instance to query.
        todo_id: The ID of the todo to retrieve.

    Returns:
        The Todo if found, None otherwise.
    """
    return store.get(todo_id)


def update_todo(
    store: TodoStore,
    todo_id: int,
    title: str | None = None,
    description: str | None = None,
) -> Todo | None:
    """Update an existing todo's title and/or description.

    Args:
        store: The TodoStore instance.
        todo_id: The ID of the todo to update.
        title: New title (None = keep existing, empty string not allowed).
        description: New description (None = keep existing).

    Returns:
        The updated Todo if found, None otherwise.

    Raises:
        ValueError: If title is provided but empty or whitespace-only.
    """
    if title is not None:
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty")

    if description is not None:
        description = description.strip()

    return store.update(todo_id, title=title, description=description)


def delete_todo(store: TodoStore, todo_id: int) -> bool:
    """Delete a todo by ID.

    Args:
        store: The TodoStore instance.
        todo_id: The ID of the todo to delete.

    Returns:
        True if deleted, False if not found.
    """
    return store.delete(todo_id)


def toggle_complete(store: TodoStore, todo_id: int) -> Todo | None:
    """Toggle a todo's completion status.

    If the todo is incomplete, marks it complete.
    If the todo is complete, marks it incomplete.

    Args:
        store: The TodoStore instance.
        todo_id: The ID of the todo to toggle.

    Returns:
        The updated Todo if found, None otherwise.
    """
    todo = store.get(todo_id)
    if todo is None:
        return None

    return store.set_completed(todo_id, not todo.completed)


def set_complete(store: TodoStore, todo_id: int, completed: bool) -> Todo | None:
    """Set a todo's completion status to a specific value.

    Args:
        store: The TodoStore instance.
        todo_id: The ID of the todo to update.
        completed: The new completion status.

    Returns:
        The updated Todo if found, None otherwise.
    """
    return store.set_completed(todo_id, completed)
