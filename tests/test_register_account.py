from pages.register_page import RegisterPage

def test_registration_success(browser, base_url, fake_user):
    page = RegisterPage(browser)
    page.register_page_open(base_url)
    page.fill_registration_form(
        fake_user["first_name"],
        fake_user["last_name"],
        fake_user["email"],
        fake_user["password"],
    )

    assert page.is_account_created_successfully(), "Account creation message not found!"