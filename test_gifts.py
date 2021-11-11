import pytest
from gifts import Gift


@pytest.fixture
def my_local_gift():
    return Gift(1, 1, 10)


def test_my_gift_paper(my_gift):
    assert my_gift.wrapping_paper() == 58


def test_my_gift_ribbon(my_gift):
    assert my_gift.wrapping_ribbon() == 34


def test_my_local_gift_paper(my_local_gift):
    assert my_local_gift.wrapping_paper() == 43


def test_my_local_gift_ribbon(my_local_gift):
    assert my_local_gift.wrapping_ribbon() == 14