import pytest

from todo.models import Task


@pytest.mark.django_db
def test_task_str():
    task = Task.objects.create(title="Aprender Tox")
    assert str(task) == "Aprender Tox"
