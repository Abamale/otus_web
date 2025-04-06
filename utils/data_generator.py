import random

from faker import Faker

class DataGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_user_data(self):
        return {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "email": self.faker.unique.email(),
            "password": self.faker.password(length=10),
        }

    def generate_products_data(self):
        return {
            "product_name": f"{self.faker.word()}_{random.randint(9, 9999999)}",
            "meta_tag_title": self.faker.word(),
            "model": self.faker.word(),
            "keyword": self.faker.slug()
        }