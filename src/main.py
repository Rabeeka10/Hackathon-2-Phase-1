"""Application entry point and main loop.

This module contains the main application logic that coordinates
between the CLI interface and business services. It handles the
main menu loop, dispatches user choices to appropriate handlers,
and manages graceful shutdown.
"""

from src import cli, services
from src.store import TodoStore


def handle_add_task(store: TodoStore) -> None:
    """Handle the add task flow.

    Prompts user for title and description, creates the task,
    and displays confirmation.

    Args:
        store: The TodoStore instance.
    """
    title = cli.prompt_for_title()
    description = cli.prompt_for_description()

    try:
        todo = services.create_todo(store, title, description)
        cli.display_success(f"Task added successfully! (ID: {todo.id})")
    except ValueError as e:
        cli.display_error(str(e))


def handle_view_tasks(store: TodoStore) -> None:
    """Handle the view tasks flow.

    Retrieves all tasks and displays them.

    Args:
        store: The TodoStore instance.
    """
    todos = services.list_todos(store)
    cli.display_todos(todos)


def handle_mark_complete(store: TodoStore) -> None:
    """Handle marking a task as complete.

    Prompts for task ID and marks it complete.

    Args:
        store: The TodoStore instance.
    """
    todo_id = cli.prompt_for_id()
    todo = services.set_complete(store, todo_id, completed=True)

    if todo is None:
        cli.display_error(f"Task with ID {todo_id} not found.")
    else:
        cli.display_success("Task marked as complete!")


def handle_mark_incomplete(store: TodoStore) -> None:
    """Handle marking a task as incomplete.

    Prompts for task ID and marks it incomplete.

    Args:
        store: The TodoStore instance.
    """
    todo_id = cli.prompt_for_id()
    todo = services.set_complete(store, todo_id, completed=False)

    if todo is None:
        cli.display_error(f"Task with ID {todo_id} not found.")
    else:
        cli.display_success("Task marked as incomplete!")


def handle_update_task(store: TodoStore) -> None:
    """Handle updating a task's details.

    Prompts for task ID, then for new title and description.
    User can press Enter to keep current values.

    Args:
        store: The TodoStore instance.
    """
    todo_id = cli.prompt_for_id()
    todo = services.get_todo(store, todo_id)

    if todo is None:
        cli.display_error(f"Task with ID {todo_id} not found.")
        return

    print()
    new_title = cli.prompt_for_update_title(todo.title)
    new_description = cli.prompt_for_update_description(todo.description)

    # Only update if at least one field changed
    if new_title is None and new_description is None:
        cli.display_success("No changes made.")
        return

    try:
        updated_todo = services.update_todo(
            store, todo_id, title=new_title, description=new_description
        )
        if updated_todo:
            cli.display_success("Task updated successfully!")
        else:
            cli.display_error(f"Task with ID {todo_id} not found.")
    except ValueError as e:
        cli.display_error(str(e))


def handle_delete_task(store: TodoStore) -> None:
    """Handle deleting a task.

    Prompts for task ID and deletes the task.

    Args:
        store: The TodoStore instance.
    """
    todo_id = cli.prompt_for_id()
    success = services.delete_todo(store, todo_id)

    if success:
        cli.display_success("Task deleted successfully!")
    else:
        cli.display_error(f"Task with ID {todo_id} not found.")


def main() -> None:
    """Main application entry point.

    Initializes the store and runs the main menu loop until
    the user chooses to exit or presses Ctrl+C.
    """
    store = TodoStore()

    try:
        while True:
            cli.display_menu()
            choice = cli.get_menu_choice()

            if choice == 1:
                handle_add_task(store)
            elif choice == 2:
                handle_view_tasks(store)
            elif choice == 3:
                handle_update_task(store)
            elif choice == 4:
                handle_delete_task(store)
            elif choice == 5:
                handle_mark_complete(store)
            elif choice == 6:
                handle_mark_incomplete(store)
            elif choice == 7:
                cli.display_goodbye()
                break

    except KeyboardInterrupt:
        cli.display_goodbye()


if __name__ == "__main__":
    main()
