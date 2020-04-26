from fixture.session import SessionHelper
from selenium import webdriver
import os


class Application:

    def __init__(self):
        self.wd = self.run_webdriver_chrome()
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://addressbook/")

    def run_webdriver_chrome(self):
        path = os.path.dirname(os.path.abspath(__file__))
        path = path + "/chromedriver"
        wd = webdriver.Chrome(executable_path=path)
        wd.implicitly_wait(60)
        return wd

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
#
    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def destroy(self):
        self.wd.quit()
