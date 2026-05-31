## To-Do App Specification
Function: add_task(task: str)
Function: remove_task(task: str)
Function: list_tasks()
Function: mark_complete(task: str)

Rules:
- Tasks stored in a list
- Cannot add duplicate tasks
- Cannot remove tasks that doesn't exist
- mark_complete adds [DONE] to task name
- list_tasks returns all tasks

Edge cases:
- Empty string task -> reject
- None -> reject
- Already complete task -> don't mark again