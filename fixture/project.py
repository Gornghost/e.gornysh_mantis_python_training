class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # Click New group
        wd.find_element_by_name("new").click()
        self.fill_project_form(project)
        # Click submit
        wd.find_element_by_name("submit").click()
        self.return_to_project_page()
    