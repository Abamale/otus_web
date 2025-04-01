# otus_web

Тесты запускаются командой: 
- определенный набор тестов:
pytest tests/test_admin_products_page.py --alluredir=reports/allure-results

- все тесты:
pytest tests/ --alluredir=reports/allure-results

Отчет allure формируется: allure serve reports/allure-results

"Поломанный" тест со скриншотом: test_admin_product_page/test_fail_wrong_locator