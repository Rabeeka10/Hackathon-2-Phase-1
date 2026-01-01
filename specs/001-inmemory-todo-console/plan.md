# Implementation Plan: In-Memory Todo Console Application

**Branch**: `001-inmemory-todo-console` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-inmemory-todo-console/spec.md`

## Summary

Build a Python console-based todo application that stores tasks exclusively in memory. The application provides a menu-driven interface for CRUD operations (Create, Read, Update, Delete) plus completion status toggling. Architecture follows a layered design with strict separation between business logic and console I/O to enable future extension to web/AI interfaces in Phase II and III.

## Technical Context

**Language/Version**: Python 3.13+ (as specified in constraints; compatible with 3.10+ per constitution)
**Primary Dependencies**: Python standard library only (no third-party packages)
**Storage**: In-memory only (Python list/dict data structures)
**Testing**: Manual console interaction (automated tests out of scope for Phase I)
**Target Platform**: Cross-platform console/terminal (Windows, macOS, Linux)
**Project Type**: Single project (console application)
**Performance Goals**: Response within 1 second for all operations; handle 100+ tasks without degradation
**Constraints**: No persistence, no external services, no frameworks, deterministic behavior
**Scale/Scope**: Single-user, single-session, in-memory storage only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status | Notes |
|-----------|-------------|--------|-------|
| I. Correctness-First | Deterministic behavior, exact requirements match | ✅ PASS | All operations defined with acceptance scenarios |
| II. Simplicity & Clarity | Readable, beginner-friendly code | ✅ PASS | 4-file modular structure, clear naming |
| III. In-Memory Purity | No file/DB persistence | ✅ PASS | Data structures in memory only |
| IV. Console-Native UX | Menu-driven, resilient to invalid input | ✅ PASS | Numeric menu, validation on all inputs |
| V. Extensibility by Design | Business logic separable from UI | ✅ PASS | services.py separate from cli.py |

**Technical Standards Compliance**:
- [x] Python >= 3.10 (using 3.13+)
- [x] Console/terminal execution only
- [x] Standard library only
- [x] Data model: ID, Title, Completed, Description

**Constraints Compliance**:
- [x] No file/DB persistence
- [x] No external services/APIs
- [x] No third-party frameworks
- [x] Single responsibility per function
- [x] Logic layer does not depend on I/O layer

**GATE STATUS**: ✅ PASSED - No violations. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-inmemory-todo-console/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── checklists/          # Validation checklists
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py          # Package marker
├── models.py            # Todo dataclass definition
├── store.py             # In-memory task collection with ID tracking
├── services.py          # Business logic (add, list, update, delete, toggle)
├── cli.py               # Console UI (menu, prompts, display)
└── main.py              # Application entry point and loop
```

**Structure Decision**: Single project with flat module structure. Four core modules plus entry point:
1. `models.py` - Data structures (Todo dataclass)
2. `store.py` - In-memory storage abstraction (enables future DB swap)
3. `services.py` - Business operations (pure logic, no I/O)
4. `cli.py` - Console interface (all user interaction)
5. `main.py` - Application bootstrap and main loop

This structure enables:
- Phase II: Replace `store.py` with database-backed implementation
- Phase II: Add `api.py` alongside `cli.py` for FastAPI endpoints
- Phase III: Add `chatbot.py` for AI-powered natural language interface

## Complexity Tracking

> No violations to justify. Design follows simplest viable approach.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |

## Architecture Decisions

### Decision 1: Separate Store Module

**Choice**: Create dedicated `store.py` module for in-memory storage
**Rationale**: Enables clean swap to database-backed storage in Phase II without touching business logic
**Alternatives Considered**:
- Inline storage in services.py - Rejected: couples storage to logic
- Single todos list in main.py - Rejected: violates separation of concerns

### Decision 2: Dataclass for Todo Entity

**Choice**: Use Python `dataclasses.dataclass` for Todo model
**Rationale**: Clean, type-hinted, minimal boilerplate, stdlib only
**Alternatives Considered**:
- Plain dict - Rejected: no type safety, harder to maintain
- NamedTuple - Rejected: immutable, harder to update fields
- Custom class - Rejected: unnecessary boilerplate for simple entity

### Decision 3: Menu-Driven Interface

**Choice**: Numeric menu selection (1-7 for operations)
**Rationale**: Intuitive for console apps, easy input validation, clear user guidance
**Alternatives Considered**:
- Command-based (type "add", "list") - Rejected: more parsing complexity, typo-prone

### Decision 4: Monotonic ID Generation

**Choice**: Auto-increment integer IDs, never reused after deletion
**Rationale**: Simple, deterministic, avoids confusion with reused IDs
**Alternatives Considered**:
- UUID - Rejected: overkill for in-memory, harder to type
- Reusable IDs - Rejected: creates confusion, spec prohibits reuse

## Component Design

### models.py

```python
@dataclass
class Todo:
    id: int
    title: str
    completed: bool = False
    description: str = ""
```

### store.py

```python
class TodoStore:
    _todos: dict[int, Todo]
    _next_id: int

    def add(todo_data) -> Todo
    def get(id) -> Todo | None
    def get_all() -> list[Todo]
    def update(id, **fields) -> Todo | None
    def delete(id) -> bool
```

### services.py

```python
def create_todo(store, title, description="") -> Todo
def list_todos(store) -> list[Todo]
def update_todo(store, id, title=None, description=None) -> Todo | None
def delete_todo(store, id) -> bool
def toggle_complete(store, id) -> Todo | None
```

### cli.py

```python
def display_menu() -> None
def get_menu_choice() -> int
def prompt_for_title() -> str
def prompt_for_description() -> str
def prompt_for_id() -> int
def display_todos(todos) -> None
def display_success(message) -> None
def display_error(message) -> None
```

### main.py

```python
def main() -> None:
    # Initialize store
    # Main loop: display menu, get choice, dispatch to handler
    # Handle KeyboardInterrupt gracefully
```

## Error Handling Strategy

| Error Type | Handling | User Message |
|------------|----------|--------------|
| Empty title | Reject, re-prompt | "Title cannot be empty. Please enter a title." |
| Invalid menu choice | Reject, re-prompt | "Invalid choice. Please enter a number 1-7." |
| Invalid ID format | Reject, re-prompt | "Invalid ID. Please enter a positive number." |
| Task not found | Display error, return to menu | "Task with ID {id} not found." |
| Keyboard interrupt | Graceful exit | "Goodbye!" |

## Dependencies Between Modules

```
main.py
  └── imports: cli, services, store

cli.py
  └── imports: (none - pure I/O)

services.py
  └── imports: models, store

store.py
  └── imports: models

models.py
  └── imports: dataclasses (stdlib)
```

**Key Constraint**: `cli.py` does NOT import `services.py` or `store.py`. All coordination happens in `main.py`. This ensures UI logic is completely decoupled from business logic.

## Phase Transition Readiness

### Phase II (FastAPI + SQLModel)

- Replace `store.py` implementation with SQLModel-backed version
- Add `api.py` with FastAPI endpoints calling same `services.py` functions
- Todo dataclass maps directly to SQLModel table definition

### Phase III (AI Chatbot)

- Add `chatbot.py` with natural language parsing
- Chatbot calls same `services.py` functions
- No changes to core business logic required
