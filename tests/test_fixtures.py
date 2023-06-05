import pytest


@pytest.fixture
def chrome(browser):
    pass


@pytest.fixture(scope="module")
def user_id():
    return 123


def test_auth(chrome, user_id):
    assert user_id == 123


def test_second(user_id, chrome):
    assert user_id == 123

