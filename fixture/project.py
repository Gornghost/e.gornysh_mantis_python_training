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
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache)