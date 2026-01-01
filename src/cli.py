"""Console user interface for the todo application.

This module contains all functions for user interaction via the console.
It handles menu display, user prompts, input validation, and output
formatting. This module has no dependencies on business logic or storage.
"""

from src.models import Todo


def display_menu() -> None:
    """Display the main menu with numbered options."""
    print()
    print("=" * 30)
    print("       TODO APP")
    print("=" * 30)
    print()
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark complete")
    print("6. Mark incomplete")
    print("7. Exit")
    print()


def get_menu_choice() -> int:
    """Get and validate menu choice from user.

    Loops until user enters a valid choice (1-7).

    Returns:
        Integer choice between 1 and 7.
    """
    while True:
        try:
            choice_str = input("Enter choice (1-7): ").strip()
            choice = int(choice_str)
            if 1 <= choice <= 7:
                return choice
            display_error("Invalid choice. Please enter a number 1-7.")
        except ValueError:
            display_error("Invalid input. Please enter a number 1-7.")


def prompt_for_title() -> str:
    """Prompt user for a task title.

    Loops until user enters a non-empty title.

    Returns:
        Non-empty stripped title string.
    """
    while True:
        title = input("Enter task title: ").strip()
        if title:
            return title
        display_error("Title cannot be empty. Please enter a title.")


def prompt_for_description() -> str:
    """Prompt user for an optional task description.

    Returns:
        Description string (may be empty).
    """
    description = input("Enter description (optional, press Enter to skip): ")
    return description.strip()


def prompt_for_id() -> int:
    """Prompt user for a task ID.

    Loops until user enters a valid positive integer.

    Returns:
        Positive integer ID.
    """
    while True:
        try:
            id_str = input("Enter task ID: ").strip()
            todo_id = int(id_str)
            if todo_id > 0:
                return todo_id
            display_error("Invalid ID. Please enter a positive number.")
        except ValueError:
            display_error("Invalid ID format. Please enter a positive number.")


def prompt_for_update_title(current_title: str) -> str | None:
    """Prompt user for updated title.

    Args:
        current_title: The current title to display.

    Returns:
        New title if provided, None if user pressed Enter to keep current.
    """
    print(f"Current title: {current_title}")
    new_title = input("Enter new title (press Enter to keep current): ").strip()
    if new_title:
        return new_title
    return None


def prompt_for_update_description(current_description: str) -> str | None:
    """Prompt user for updated description.

    Args:
        current_description: The current description to display.

    Returns:
        New description if provided, None if user pressed Enter to keep current.
    """
    if current_description:
        print(f"Current description: {current_description}")
    else:
        print("Current description: (none)")
    new_desc = input("Enter new description (press Enter to keep current): ").strip()
    if new_desc:
        return new_desc
    return None


def display_todos(todos: list[Todo]) -> None:
    """Display a formatted list of todos.

    Args:
        todos: List of Todo objects to display.
    """
    if not todos:
        print()
        print("No tasks found. Add a task to get started!")
        return

    print()
    print("=" * 40)
    print("         YOUR TASKS")
    print("=" * 40)
    print()

    complete_count = 0
    for todo in todos:
        status = "[x]" if todo.completed else "[ ]"
        if todo.completed:
            complete_count += 1

        print(f"{status} {todo.id}. {todo.title}")
        if todo.description:
            print(f"      {todo.description}")

    print()
    incomplete_count = len(todos) - complete_count
    print(f"Total: {len(todos)} tasks ({complete_count} complete, {incomplete_count} incomplete)")


def display_success(message: str) -> None:
    """Display a success message.

    Args:
        message: The success message to display.
    """
    print()
    print(f"[SUCCESS] {message}")


def display_error(message: str) -> None:
    """Display an error message.

    Args:
        message: The error message to display.
    """
    print()
    print(f"[ERROR] {message}")


def display_goodbye() -> None:
    """Display goodbye message when exiting."""
    print()
    print("Goodbye!")
