import pytest
from pages.admin_login_page import AdminLoginPage


def test_admin_login(admin_login_page, admin_credentials):
    admin_login_page.login(admin_credentials["username"], admin_credentials["password"])
    assert admin_login_page.is_logged_in(), "Admin login failed"

def test_admin_logout(admin_login_page, admin_credentials):
    admin_login_page.login(admin_credentials["username"], admin_credentials["password"])
    admin_login_page.logout()
    assert admin_login_page.is_logged_out()