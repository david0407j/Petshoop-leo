from django.urls import reverse
import pytest
from pet.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse("base:base"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(
        resp, "<title>PetShop Leo - Seu Melhor Amigo Merece o Melhor</title>"
    )


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:petleo@petshop.com"')


def test_icon_shop(
    resp,
):
    assert_contains(
        resp,
        "{% static 'img/shop.ico' %}",
    )
