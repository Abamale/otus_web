
REGISTER_SUCCESS_DATA = [
    {"email": "eve.holt@reqres.in", "password": "pistol"},
    {"email": "eve.holt@reqres.in", "password": "123456"},   # password только цифры
    {"email": "eve.holt@reqres.in", "password": "9876543210"}, # длинный числовой пароль
    {"email": "eve.holtaaa@reqres.in", "password": "pistol"}  #email отличается от тестового
]

REGISTER_UNSUCCESSFUL_DATA = [
    {"email": "sydney@fife"},
    {"email": "eve.holt@reqres.in"},  # email без password
    {"email": ""},                     # пустой email
]

LOGIN_SUCCESS_DATA = [
    {"email": "eve.holt@reqres.in", "password": "cityslicka"},
]

LOGIN_UNSUCCESS_DATA = [
    {"email": "peter@klaven"},
]