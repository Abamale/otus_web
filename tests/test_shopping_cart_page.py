from pages.shopping_cart_page import ShoppingCart


def test_is_shopping_cart_present(browser, base_url):
    page = ShoppingCart(browser)
    page.open(base_url)
    page.shopping_cart_open()
    assert page.is_shopping_cart_present(page.CONTENT), "Shopping cart content not found!"

