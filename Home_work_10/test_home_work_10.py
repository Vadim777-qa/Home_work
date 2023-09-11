import requests
import pytest

user_credentials_1 = [
    ("Poul", "Soul", "somemail@hidsf.com", "Paass_123", "Paass_123")
]


@pytest.mark.parametrize("name, last_name, email, password, repeat_password", user_credentials_1)
def test_user_is_created(name, last_name, email, password, repeat_password):
    sign_up_dict = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }

    session = requests.session()
    create_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=sign_up_dict)
    assert create_user.status_code == 201


user_credentials_2 = [
    ("uyufeyr@hidsf.com", "Paass_123", False)
]


@pytest.mark.parametrize("email, password, remember", user_credentials_2)
def test_user_is_signed_in(email, password, remember):
    sign_in_dict = {
        "email": email,
        "password": password,
        "remember": remember
    }
    session = requests.session()
    login_user = session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=sign_in_dict)
    assert login_user.status_code == 200


wrong_user_credentials = [
    ("uyufeegdfgyr@hidsf.com", "P3434_123", False)
]


@pytest.mark.parametrize("email, password, remember", wrong_user_credentials)
def test_wrong_credentials(email, password, remember):
    user_data = {
        "email": email,
        "password": password,
        "remember": remember
    }
    session = requests.session()
    login_user = session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_data)
    assert login_user.status_code == 400
