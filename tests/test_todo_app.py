import pytest

from exercise import TodoApp, add_task, remove_task, list_tasks, mark_complete


def test_add_task_stores_task():
    app = TodoApp()
    app.add_task("Write tests")
    assert app.list_tasks() == ["Write tests"]


def test_add_duplicate_task_raises():
    app = TodoApp()
    app.add_task("Write tests")
    with pytest.raises(ValueError):
        app.add_task("Write tests")


def test_add_empty_task_rejects():
    app = TodoApp()
    with pytest.raises(ValueError):
        app.add_task("")


def test_add_none_task_rejects():
    app = TodoApp()
    with pytest.raises(TypeError):
        app.add_task(None)


def test_remove_task_removes_existing():
    app = TodoApp()
    app.add_task("Buy milk")
    app.remove_task("Buy milk")
    assert app.list_tasks() == []


def test_remove_nonexistent_task_raises():
    app = TodoApp()
    with pytest.raises(ValueError):
        app.remove_task("Nonexistent")


def test_mark_complete_appends_done():
    app = TodoApp()
    app.add_task("Buy milk")
    app.mark_complete("Buy milk")
    assert app.list_tasks() == ["Buy milk [DONE]"]


def test_mark_complete_does_not_duplicate_done_marker():
    app = TodoApp()
    app.add_task("Buy milk [DONE]")
    app.mark_complete("Buy milk [DONE]")
    assert app.list_tasks() == ["Buy milk [DONE]"]


def test_list_tasks_returns_all_tasks():
    app = TodoApp()
    app.add_task("Task 1")
    app.add_task("Task 2")
    assert app.list_tasks() == ["Task 1", "Task 2"]


def test_module_level_functions_work():
    # ensure the module-level todo_app wrappers behave correctly
    add_task("Module task")
    assert "Module task" in list_tasks()
    mark_complete("Module task")
    assert "Module task [DONE]" in list_tasks()
    remove_task("Module task [DONE]")
    assert "Module task [DONE]" not in list_tasks()
