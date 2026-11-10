import json
import sqlite3
import pytest

from app import create_app, export_tasks

@pytest.fixture
def resources(tmp_path):
    db_path = tmp_path / "tasks.db"
    export_path = tmp_path / "tasks.json"
    app = create_app(db_path, export_path)

    return app.test_client(), db_path, export_path

def test_create_task(resources):
    client, db_path, export_path = resources

    response = client.post(
        "/tasks", json={"title": "Вивчити pytest"}
    )

    assert response.status_code == 201
    assert response.get_json()["title"] == "Вивчити pytest"

    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            "SELECT title FROM tasks"
        ).fetchone()

    assert row == ("Вивчити pytest",)

    data = json.loads(export_path.read_text(encoding="utf-8"))
    assert data[0]["title"] == "Вивчити pytest"

def test_get_tasks(resources):
    client, _, _ = resources

    client.post("/tasks", json={"title": "Перше завдання"})
    client.post("/tasks", json={"title": "Друге завдання"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.get_json()] == [
        "Перше завдання",
        "Друге завдання",
    ]

def test_create_task_requires_title(resources):
    client, _, export_path = resources
    response = client.post("/tasks", json={})
    assert response.status_code == 400
    assert not export_path.exists()

def test_export_empty_list(resources):
    _, db_path, export_path = resources
    export_tasks(db_path, export_path)
    data = json.loads(export_path.read_text(encoding="utf-8"))
    assert data == []

def test_export_overwrites_corrupted_json(resources):
    _, db_path, export_path = resources
    export_path.write_text("{ пошкоджений JSON", encoding="utf-8")
    export_tasks(db_path, export_path)
    data = json.loads(export_path.read_text(encoding="utf-8"))
    assert data == []

def test_two_tasks_database_order(resources):
    client, db_path, _ = resources

    client.post("/tasks", json={"title": "Перше завдання"})
    client.post("/tasks", json={"title": "Друге завдання"})

    with sqlite3.connect(db_path) as connection:
        rows = connection.execute(
            "SELECT title FROM tasks ORDER BY id"
        ).fetchall()

    assert rows == [
        ("Перше завдання",),
        ("Друге завдання",),
    ]

def test_delete_task(resources):
    client, db_path, export_path = resources
    create_response = client.post(
        "/tasks", json={"title": "Завдання для видалення"}
    )
    task_id = create_response.get_json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Завдання видалено"
    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    assert row is None
    data = json.loads(export_path.read_text(encoding="utf-8"))
    assert data == []
