# Service Interface Contract: In-Memory Todo Application

**Feature**: 001-inmemory-todo-console
**Date**: 2026-01-01
**Status**: Complete

## Overview

This document defines the contract for the service layer functions. Since Phase I is a console application (not an API), these contracts define the function signatures and behaviors that the CLI will call.

Note: This contract is designed to map directly to REST API endpoints in Phase II.

## Service Functions

### create_todo

Creates a new todo item.

**Signature**:
```python
def create_todo(store: TodoStore, title: str, description: str = "") -> Todo
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |
| title | str | Yes | Task title (must be non-empty) |
| description | str | No | Optional task description |

**Returns**: `Todo` - The newly created todo with auto-assigned ID

**Raises**: `ValueError` if title is empty

**Example**:
```python
todo = create_todo(store, "Buy groceries", "From farmer's market")
# Returns: Todo(id=1, title="Buy groceries", completed=False, description="From farmer's market")
```

**Phase II Mapping**: `POST /todos`

---

### list_todos

Retrieves all todos.

**Signature**:
```python
def list_todos(store: TodoStore) -> list[Todo]
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |

**Returns**: `list[Todo]` - All todos in insertion order (empty list if none)

**Example**:
```python
todos = list_todos(store)
# Returns: [Todo(id=1, ...), Todo(id=2, ...)]
```

**Phase II Mapping**: `GET /todos`

---

### get_todo

Retrieves a single todo by ID.

**Signature**:
```python
def get_todo(store: TodoStore, todo_id: int) -> Todo | None
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |
| todo_id | int | Yes | ID of the todo to retrieve |

**Returns**: `Todo | None` - The todo if found, None otherwise

**Example**:
```python
todo = get_todo(store, 1)
# Returns: Todo(id=1, ...) or None
```

**Phase II Mapping**: `GET /todos/{id}`

---

### update_todo

Updates an existing todo's title and/or description.

**Signature**:
```python
def update_todo(
    store: TodoStore,
    todo_id: int,
    title: str | None = None,
    description: str | None = None
) -> Todo | None
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |
| todo_id | int | Yes | ID of the todo to update |
| title | str \| None | No | New title (None = keep existing) |
| description | str \| None | No | New description (None = keep existing) |

**Returns**: `Todo | None` - Updated todo if found, None if not found

**Raises**: `ValueError` if title is provided but empty

**Example**:
```python
todo = update_todo(store, 1, title="Buy vegetables")
# Returns: Todo(id=1, title="Buy vegetables", ...) or None
```

**Phase II Mapping**: `PATCH /todos/{id}`

---

### delete_todo

Permanently removes a todo.

**Signature**:
```python
def delete_todo(store: TodoStore, todo_id: int) -> bool
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |
| todo_id | int | Yes | ID of the todo to delete |

**Returns**: `bool` - True if deleted, False if not found

**Example**:
```python
success = delete_todo(store, 1)
# Returns: True or False
```

**Phase II Mapping**: `DELETE /todos/{id}`

---

### toggle_complete

Toggles a todo's completion status.

**Signature**:
```python
def toggle_complete(store: TodoStore, todo_id: int) -> Todo | None
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |
| todo_id | int | Yes | ID of the todo to toggle |

**Returns**: `Todo | None` - Updated todo if found, None if not found

**Behavior**: If `completed=False`, sets to `True`. If `completed=True`, sets to `False`.

**Example**:
```python
todo = toggle_complete(store, 1)
# If was completed=False, now completed=True
# Returns: Todo(id=1, completed=True, ...) or None
```

**Phase II Mapping**: `PATCH /todos/{id}/toggle`

---

### set_complete

Explicitly sets a todo's completion status.

**Signature**:
```python
def set_complete(store: TodoStore, todo_id: int, completed: bool) -> Todo | None
```

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | TodoStore | Yes | The in-memory store instance |
| todo_id | int | Yes | ID of the todo to update |
| completed | bool | Yes | New completion status |

**Returns**: `Todo | None` - Updated todo if found, None if not found

**Example**:
```python
todo = set_complete(store, 1, True)
# Returns: Todo(id=1, completed=True, ...) or None
```

**Phase II Mapping**: `PATCH /todos/{id}` with `{"completed": true}`

## Error Handling

| Scenario | Service Response | CLI Display |
|----------|------------------|-------------|
| Empty title on create | Raise ValueError | "Title cannot be empty" |
| Empty title on update | Raise ValueError | "Title cannot be empty" |
| Todo not found | Return None | "Task with ID {id} not found" |
| Delete not found | Return False | "Task with ID {id} not found" |

## Invariants

1. **ID Uniqueness**: No two todos ever have the same ID
2. **ID Immutability**: A todo's ID never changes after creation
3. **ID Non-Reuse**: Deleted IDs are never reassigned
4. **Determinism**: Same operations on same state produce same results
