from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # Click New group
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        # Click submit
        wd.find_element_by_xpath("//input[@class='button']").click()
        self.open_projects_page()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_xpath(".//input[@value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys(project.name)
        self.change_select_list_value("status", project.status)
        if not wd.find_element_by_name("inherit_global").get_attribute("checked"):
            wd.find_element_by_name("inherit_global").click()
        self.change_select_list_value("view_state", project.view_status)
        wd.find_element_by_name("description").send_keys(project.description)

    def change_select_list_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            select_list = wd.find_element_by_name(field_name)
            select_list.find_element_by_xpath(".//option[text()='%s']" % value).click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        self.project_list = []
        projects = wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit_page')]/../..")
        for element in projects:
            projects = element.find_elements_by_tag_name("td")
            name = projects[0].find_element_by_tag_name("a").text.strip()
            status = projects[1].text.strip()
            view_status = projects[3].text.strip()
            description = projects[4].text.strip()
            self.project_list.append(Project(name=name, status=status, view_status=view_status, description=description))
        return list(self.project_list)

    def delete_project_by_name(self, name):
        self.open_projects_page()
        self.open_project_by_name(name)
        self.submit_project_deletion()
        self.submit_project_deletion()
        self.open_projects_page()

    def submit_project_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//input[@value='Delete Project']").click()

    def open_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("%s" % name).click()