# Tasks: In-Memory Todo Console Application

**Input**: Design documents from `/specs/001-inmemory-todo-console/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Not included (automated tests out of scope per spec.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/` at repository root
- All source files go in `src/` directory

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create src/ directory and src/__init__.py package marker
- [x] T002 Create pyproject.toml with Python 3.13+ requirement (no dependencies)

**Checkpoint**: Project structure ready for implementation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Create Todo dataclass in src/models.py with fields: id (int), title (str), completed (bool), description (str)
- [x] T004 Create TodoStore class in src/store.py with _todos dict and _next_id counter
- [x] T005 Implement TodoStore.add() method in src/store.py - creates Todo with auto-assigned ID
- [x] T006 Implement TodoStore.get() method in src/store.py - returns Todo by ID or None
- [x] T007 Implement TodoStore.get_all() method in src/store.py - returns list of all Todos
- [x] T008 Implement TodoStore.update() method in src/store.py - updates fields by ID
- [x] T009 Implement TodoStore.delete() method in src/store.py - removes Todo by ID
- [x] T010 Implement TodoStore.set_completed() method in src/store.py - sets completion status

**Checkpoint**: Foundation ready - data model and storage operational. User story implementation can now begin.

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks with title and optional description

**Independent Test**: Launch app, select "Add task", enter title and description, verify task appears in list

### Implementation for User Story 1

- [x] T011 [US1] Implement create_todo() function in src/services.py - validates title, calls store.add()
- [x] T012 [US1] Implement display_menu() function in src/cli.py - shows numbered menu options 1-7
- [x] T013 [US1] Implement prompt_for_title() function in src/cli.py - loops until non-empty title entered
- [x] T014 [US1] Implement prompt_for_description() function in src/cli.py - accepts optional input
- [x] T015 [US1] Implement display_success() function in src/cli.py - prints success messages
- [x] T016 [US1] Implement display_error() function in src/cli.py - prints error messages
- [x] T017 [US1] Implement handle_add_task() function in src/main.py - orchestrates add flow with CLI and services

**Checkpoint**: User Story 1 complete - users can add tasks. Independently testable.

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can view all tasks in a formatted list with status indicators

**Independent Test**: Add several tasks, select "View tasks", verify all tasks displayed with IDs and status

### Implementation for User Story 2

- [x] T018 [US2] Implement list_todos() function in src/services.py - returns all todos from store
- [x] T019 [US2] Implement display_todos() function in src/cli.py - formats list with [ ]/[x] status, ID, title, description
- [x] T020 [US2] Implement handle_view_tasks() function in src/main.py - orchestrates view flow, handles empty list message

**Checkpoint**: User Stories 1 & 2 complete - MVP functional. Users can add and view tasks.

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status by ID

**Independent Test**: Add task, mark complete, verify status changed, mark incomplete, verify status reverted

### Implementation for User Story 3

- [x] T021 [US3] Implement toggle_complete() function in src/services.py - toggles completed field
- [x] T022 [US3] Implement set_complete() function in src/services.py - sets completed to specific value
- [x] T023 [US3] Implement prompt_for_id() function in src/cli.py - validates positive integer input
- [x] T024 [US3] Implement handle_mark_complete() function in src/main.py - orchestrates mark complete flow
- [x] T025 [US3] Implement handle_mark_incomplete() function in src/main.py - orchestrates mark incomplete flow

**Checkpoint**: User Story 3 complete - users can toggle completion status.

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Users can update title and/or description of existing tasks

**Independent Test**: Add task, update title, verify change persisted, update description, verify change

### Implementation for User Story 4

- [x] T026 [US4] Implement update_todo() function in src/services.py - updates title and/or description by ID
- [x] T027 [US4] Implement prompt_for_update_title() function in src/cli.py - shows current value, accepts new or Enter to keep
- [x] T028 [US4] Implement prompt_for_update_description() function in src/cli.py - shows current value, accepts new or Enter to keep
- [x] T029 [US4] Implement handle_update_task() function in src/main.py - orchestrates update flow

**Checkpoint**: User Story 4 complete - users can update task details.

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Users can permanently delete tasks by ID

**Independent Test**: Add task, delete by ID, verify task no longer appears in list

### Implementation for User Story 5

- [x] T030 [US5] Implement delete_todo() function in src/services.py - removes todo from store by ID
- [x] T031 [US5] Implement handle_delete_task() function in src/main.py - orchestrates delete flow with confirmation

**Checkpoint**: User Story 5 complete - users can delete tasks.

---

## Phase 8: User Story 6 - Exit Application (Priority: P3)

**Goal**: Users can gracefully exit the application

**Independent Test**: Select "Exit", verify goodbye message displayed and app terminates

### Implementation for User Story 6

- [x] T032 [US6] Implement display_goodbye() function in src/cli.py - prints farewell message
- [x] T033 [US6] Implement get_menu_choice() function in src/cli.py - validates input 1-7, handles invalid input
- [x] T034 [US6] Implement main() function in src/main.py - main loop with menu dispatch, KeyboardInterrupt handling
- [x] T035 [US6] Add if __name__ == "__main__" block in src/main.py - entry point

**Checkpoint**: User Story 6 complete - application has complete lifecycle.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup

- [x] T036 Verify all error messages match spec requirements in src/cli.py
- [x] T037 Verify ID never reused after deletion in src/store.py
- [x] T038 Test keyboard interrupt (Ctrl+C) handling in src/main.py
- [x] T039 Validate against quickstart.md scenarios - run full user session
- [x] T040 Verify code readability - each function understandable in 60 seconds

**Checkpoint**: All success criteria validated. Phase I complete.

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup
    ↓
Phase 2: Foundational (BLOCKS all user stories)
    ↓
Phase 3: US1 Add Task ─────┬─→ Phase 4: US2 View Tasks (MVP complete)
                           │
                           ├─→ Phase 5: US3 Toggle Complete
                           │
                           ├─→ Phase 6: US4 Update Task
                           │
                           ├─→ Phase 7: US5 Delete Task
                           │
                           └─→ Phase 8: US6 Exit App
                                      ↓
                               Phase 9: Polish
```

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Phase 2 completion. No dependencies on other stories.
- **User Story 2 (P1)**: Depends on Phase 2. Uses display functions, independent of US1 for testing.
- **User Story 3 (P2)**: Depends on Phase 2. Requires tasks to exist (uses US1 in practice).
- **User Story 4 (P2)**: Depends on Phase 2. Requires tasks to exist (uses US1 in practice).
- **User Story 5 (P3)**: Depends on Phase 2. Requires tasks to exist (uses US1 in practice).
- **User Story 6 (P3)**: Depends on CLI functions from earlier phases.

### Within Each User Story

1. Services function first (business logic)
2. CLI functions second (user interface)
3. Main handler last (orchestration)

### Parallel Opportunities

Within Phase 2 (Foundational):
```
T003 (models.py) → T004, T005, T006, T007, T008, T009, T010 (all in store.py, sequential)
```

Within Phase 3-8:
- Each user story can be implemented sequentially
- If multiple developers: different user stories can run in parallel after Phase 2

---

## Parallel Example: Foundational Phase

```bash
# T003 must complete first (models.py needed by store.py)
Task: "Create Todo dataclass in src/models.py"

# Then store.py tasks are sequential (same file)
Task: "Create TodoStore class in src/store.py"
Task: "Implement TodoStore.add() method in src/store.py"
# ... etc
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test add + view flow
6. Demo MVP if ready

### Full Feature Delivery

1. Complete MVP (Setup + Foundational + US1 + US2)
2. Add User Story 3 (Toggle Complete) → Test
3. Add User Story 4 (Update Task) → Test
4. Add User Story 5 (Delete Task) → Test
5. Add User Story 6 (Exit App) → Test
6. Complete Phase 9: Polish

### Agentic Execution (Claude Code)

Execute tasks sequentially via Claude Code:
1. Each task generates/modifies exactly one file
2. Commit after each task or logical group
3. Validate at each checkpoint before proceeding

---

## Summary

| Metric | Count |
|--------|-------|
| Total Tasks | 40 |
| Setup Tasks | 2 |
| Foundational Tasks | 8 |
| US1 Tasks | 7 |
| US2 Tasks | 3 |
| US3 Tasks | 5 |
| US4 Tasks | 4 |
| US5 Tasks | 2 |
| US6 Tasks | 4 |
| Polish Tasks | 5 |

**MVP Scope**: Phases 1-4 (20 tasks) - Setup + Foundational + Add Task + View Tasks

**Files Created**:
- `src/__init__.py`
- `src/models.py`
- `src/store.py`
- `src/services.py`
- `src/cli.py`
- `src/main.py`
- `pyproject.toml`

---

## Notes

- [P] marker not used because most tasks are sequential within phases
- [Story] label maps task to specific user story for traceability
- Each user story is independently testable after completion
- No automated tests (per spec.md Out of Scope section)
- All code generated via Claude Code - no manual edits
- Commit after each task or logical group
