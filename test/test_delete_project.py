from model.project import Project
import random


def test_delete_random_contact(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test_prj_name", description="test_prj_description"))
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project_by_name(project.name)
    new_list = app.project.get_project_list()
    old_list.remove(project)
    assert sorted(old_list, key=Project.by_name) == sorted(new_list, key=Project.by_name)