import pytest
from pages.admin_login_page import AdminLoginPage


def test_admin_login(browser, base_url, admin_credentials):
    page = AdminLoginPage(browser)
    page.admin_page_open(base_url)
    page.login(admin_credentials["username"], admin_credentials["password"])

    assert page.is_logged_in(), "Admin login failed"

def test_admin_logout(browser, base_url, admin_credentials):
    page = AdminLoginPage(browser)
    page.admin_page_open(base_url)
    page.login(admin_credentials["username"], admin_credentials["password"])
    page.logout()

    assert page.is_logged_out()