from pages.admin_products_page import AdminProductsPage


def test_is_product_page_present(product_page):
    assert product_page.is_products_page_present(), "Страница с товарами не открыта"

def test_new_product_form_present(product_page):
    product_page.add_new_product_form()
    assert product_page.is_new_product_form_present(), "Форма карточки товара не открылась"

def test_is_new_product_added(product_page, fake_product):
    product_page.add_new_product(fake_product)
    assert product_page.is_new_product_added(fake_product), "Товар не создан"

def test_is_product_deleted(product_page, fake_product):
    product_page.add_new_product(fake_product)
    product_page.delete_product(fake_product)
    assert not product_page.is_new_product_added(fake_product), "Товар не был удален"