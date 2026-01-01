# Research: In-Memory Todo Console Application

**Feature**: 001-inmemory-todo-console
**Date**: 2026-01-01
**Status**: Complete

## Overview

This document captures technical research and decisions made during Phase 0 of planning. Since the feature specification and constitution were comprehensive, no "NEEDS CLARIFICATION" items remained. This research documents best practices and implementation patterns selected.

## Research Topics

### 1. Python Data Structures for Todo Storage

**Question**: What is the best in-memory data structure for storing todos with fast ID lookup?

**Decision**: `dict[int, Todo]` (dictionary with integer keys)

**Rationale**:
- O(1) lookup by ID for get, update, delete operations
- O(n) for list all (acceptable for <1000 items)
- Native Python, no dependencies
- Maintains insertion order in Python 3.7+

**Alternatives Considered**:
- `list[Todo]` - O(n) lookup by ID, rejected for performance
- `OrderedDict` - Redundant in Python 3.7+, dict already ordered

### 2. Python Dataclass vs Alternatives

**Question**: What is the best way to define the Todo entity?

**Decision**: `@dataclass` from stdlib `dataclasses` module

**Rationale**:
- Built into Python stdlib (no dependencies)
- Automatic `__init__`, `__repr__`, `__eq__`
- Type hints for IDE support and documentation
- Mutable by default (needed for update operations)
- Clean, minimal syntax

**Alternatives Considered**:
- Plain dict: No type safety, harder to refactor
- NamedTuple: Immutable, can't update fields easily
- TypedDict: Less ergonomic, no instance methods
- attrs: Third-party, violates stdlib-only constraint
- Pydantic: Third-party, overkill for Phase I

### 3. Console Menu Design Patterns

**Question**: What is the best UX pattern for a console todo app?

**Decision**: Numeric menu with clear numbered options

**Rationale**:
- Simple input validation (check if input is 1-7)
- No typo issues (unlike command-based)
- Clear visual structure
- Common pattern users recognize

**Menu Structure**:
```
=== Todo App ===
1. Add task
2. List tasks
3. Update task
4. Delete task
5. Mark complete
6. Mark incomplete
7. Exit

Enter choice (1-7):
```

**Alternatives Considered**:
- Command-based ("add", "list"): More parsing, typo-prone
- Single-letter commands ("a", "l"): Less intuitive
- REPL-style: Overkill for simple CRUD

### 4. ID Generation Strategy

**Question**: How should task IDs be generated?

**Decision**: Monotonic auto-increment, starting at 1, never reused

**Rationale**:
- Simple and predictable
- Spec requirement: IDs never reused after deletion
- Easy for users to reference
- Deterministic behavior

**Implementation**:
```python
class TodoStore:
    _next_id: int = 1

    def add(self, ...) -> Todo:
        todo = Todo(id=self._next_id, ...)
        self._next_id += 1
        return todo
```

**Alternatives Considered**:
- UUID: Harder to type, overkill for in-memory
- Reuse deleted IDs: Violates spec, confusing for users
- Timestamp-based: Unnecessary complexity

### 5. Error Handling Pattern

**Question**: How should input validation errors be handled?

**Decision**: Validate at CLI layer, re-prompt on invalid input

**Rationale**:
- User-friendly: clear messages, opportunity to correct
- Separation of concerns: CLI handles I/O validation
- Services receive only valid data

**Pattern**:
```python
def prompt_for_title() -> str:
    while True:
        title = input("Enter title: ").strip()
        if title:
            return title
        print("Error: Title cannot be empty.")
```

### 6. Keyboard Interrupt Handling

**Question**: How should Ctrl+C be handled?

**Decision**: Catch `KeyboardInterrupt` in main loop, display goodbye, exit cleanly

**Rationale**:
- Spec requirement: graceful exit
- No stack trace shown to user
- Consistent with normal exit behavior

**Implementation**:
```python
def main():
    try:
        while True:
            # main loop
    except KeyboardInterrupt:
        print("\nGoodbye!")
```

### 7. Module Separation Strategy

**Question**: How should code be organized for extensibility?

**Decision**: 5-module structure with dependency inversion

**Rationale**:
- `models.py`: Pure data definitions, no dependencies
- `store.py`: Storage abstraction, depends only on models
- `services.py`: Business logic, depends on models and store interface
- `cli.py`: Pure I/O, no business logic dependencies
- `main.py`: Composition root, wires everything together

This enables:
- Phase II: Swap `store.py` for database-backed implementation
- Phase II: Add `api.py` parallel to `cli.py`
- Phase III: Add `chatbot.py` parallel to `cli.py`

## Conclusion

All technical decisions align with:
- Constitution principles (simplicity, correctness, extensibility)
- Spec requirements (all features, constraints)
- Python best practices (stdlib only, type hints, clear structure)

No unresolved questions remain. Ready for Phase 1: Design & Contracts.
