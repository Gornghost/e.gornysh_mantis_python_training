def test_add_project(app, json_projects):
    project = json_projects
    app.session.login(username="administrator", password="root")
    app.project.create(project)
    app.session.logout()