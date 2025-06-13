# otus_web

Тесты запускаются командой: 
- определенный набор тестов:
pytest tests/test_admin_products_page.py --alluredir=reports/allure-results

- все тесты:
pytest tests/ --alluredir=reports/allure-results

Отчет allure формируется: allure serve reports/allure-results

"Поломанный" тест со скриншотом: test_admin_product_page/test_fail_wrong_locator


Запуск тестов удаленно на selenoid:
Компонент	URL для доступа:
OpenCart	http://${LOCAL_IP}:8081
phpMyAdmin	http://${LOCAL_IP}:8888
Selenoid UI	http://${LOCAL_IP}:8080
Selenoid API	http://${LOCAL_IP}:4444/status

Скачать Configuration Manager:
https://aerokube.com/cm/latest/ 

команда для запуска:
./cm_linux_amd64 selenoid start
./cm_linux_amd64 selenoid-ui start

команда для остановки:
./cm_linux_amd64 selenoid stop
./cm_linux_amd64 selenoid-ui stop

посмотреть запущенные контейнеры:
docker ps 

удалить образы и настройки:
selenoid cleanup

скачать образы браузеров:
docker pull quay.io/browser/google-chrome-stable:133.0

установить количество сессий:
./cm_linux_amd64 selenoid start --args "-limit=10"

для запуска контейнера с opencart:
docker compose up -d

запуск тестов:
pytest tests/test_admin_login.py --browser=chrome --remote --alluredir=allure-results