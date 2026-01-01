# Quickstart: In-Memory Todo Console Application

**Feature**: 001-inmemory-todo-console
**Date**: 2026-01-01

## Prerequisites

- Python 3.13+ installed
- UV package manager (recommended) OR standard Python

## Installation

### Option 1: Using UV (Recommended)

```bash
# Clone or navigate to the project
cd "Phase I"

# Create virtual environment and install
uv venv
uv pip install -e .
```

### Option 2: Using Standard Python

```bash
# Clone or navigate to the project
cd "Phase I"

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# No dependencies to install (stdlib only)
```

## Running the Application

### From Project Root

```bash
# Using UV
uv run python -m src.main

# Using standard Python (with venv activated)
python -m src.main
```

### Direct Execution

```bash
# Navigate to src directory
cd src

# Run main module
python main.py
```

## Usage

When you start the application, you'll see a menu:

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

### Adding a Task

```
Enter choice (1-7): 1

Enter task title: Buy groceries
Enter description (optional, press Enter to skip): Weekly shopping

✓ Task added successfully! (ID: 1)
```

### Listing Tasks

```
Enter choice (1-7): 2

=== Your Tasks ===

[ ] 1. Buy groceries
      Weekly shopping

[x] 2. Call dentist
      Schedule annual checkup

Total: 2 tasks (1 complete, 1 incomplete)
```

### Updating a Task

```
Enter choice (1-7): 3

Enter task ID to update: 1
Enter new title (press Enter to keep current): Buy vegetables
Enter new description (press Enter to keep current):

✓ Task updated successfully!
```

### Deleting a Task

```
Enter choice (1-7): 4

Enter task ID to delete: 1

✓ Task deleted successfully!
```

### Marking Complete/Incomplete

```
Enter choice (1-7): 5

Enter task ID to mark complete: 2

✓ Task marked as complete!
```

### Exiting

```
Enter choice (1-7): 7

Goodbye!
```

Or press `Ctrl+C` at any time:

```
^C
Goodbye!
```

## Example Session

```
=== Todo App ===

1. Add task
2. List tasks
3. Update task
4. Delete task
5. Mark complete
6. Mark incomplete
7. Exit

Enter choice (1-7): 1

Enter task title: Learn Python
Enter description (optional): Complete the tutorial

✓ Task added successfully! (ID: 1)

Enter choice (1-7): 1

Enter task title: Build todo app
Enter description (optional):

✓ Task added successfully! (ID: 2)

Enter choice (1-7): 2

=== Your Tasks ===

[ ] 1. Learn Python
      Complete the tutorial

[ ] 2. Build todo app

Total: 2 tasks (0 complete, 2 incomplete)

Enter choice (1-7): 5

Enter task ID to mark complete: 1

✓ Task marked as complete!

Enter choice (1-7): 2

=== Your Tasks ===

[x] 1. Learn Python
      Complete the tutorial

[ ] 2. Build todo app

Total: 2 tasks (1 complete, 1 incomplete)

Enter choice (1-7): 7

Goodbye!
```

## Troubleshooting

### "Invalid choice" error
Enter only numbers 1-7. Don't include the period or description.

### "Title cannot be empty" error
Task titles are required. Enter at least one character.

### "Task not found" error
Check the task ID using "List tasks" (option 2). IDs are never reused.

### Application not starting
Ensure Python 3.13+ is installed: `python --version`

## Notes

- All data is stored in memory only
- Data is cleared when you exit the application
- This is Phase I - persistence comes in Phase II
