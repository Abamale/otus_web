import pytest
import re

POSITIVE_PAGES = [1, 2]
NEGATIVE_PAGES = [0, -1]

PAGE_TEST_DATA = [1, 2]
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
AVATAR_URL_PREFIX = "https://"

EXISTING_USER_IDS = [1, 2, 3]
NOT_FOUND_USER_IDS = [23, 0, -1]

CREATE_USER_TEST_DATA = [
    ("John Doe", "QA Engineer"),
    ("Alice", "Developer"),
]

UPDATE_USER_TEST_DATA = [
    ("John Doe", "QA Lead"),
    ("Alice", "Senior Developer"),
]