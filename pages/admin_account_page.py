from selenium.webdriver.common.by import By
from pages.admin_base_page import AdminBasePage

class AdminAccountPage(AdminBasePage):
    CATALOG_LINK = (By.CSS_SELECTOR, "a.parent.collapsed[href='#collapse-1']")

    pass