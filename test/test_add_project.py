from model.project import Project

def test_add_project(app, json_projects):
    project = json_projects
    old_list = app.project.get_project_list()
    app.project.create(project)
    new_list = app.project.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.by_name) == sorted(new_list, key=Project.by_name)