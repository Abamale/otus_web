import requests
import os
from dotenv import load_dotenv
import pytest

load_dotenv()

class APIClient:
    def __init__(self):
        load_dotenv()
        self.BASE_URL = os.getenv("REQRES_BASE_URL")
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36"
            ),
            "Content-type": "application/json",
            "x-api-key": "reqres-free-v1",
            "Accept": "*/*"
        })


    def get(self, endpoint, params=None):
        """GET запрос"""
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.get(url, params=params)

    def post(self, endpoint, data=None, json=None):
        """POST запрос"""
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.post(url, data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        """PUT запрос"""
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.put(url, data=data, json=json)

    def patch(self, endpoint, data=None, json=None):
        """PATCH запрос"""
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.patch(url, data=data, json=json)

    def delete(self, endpoint):
        """DELETE запрос"""
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.delete(url)


