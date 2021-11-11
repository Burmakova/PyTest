import pytest
from gifts import Gift


def test_all_gifts_paper(gifts):
    assert len(gifts) == 1000
    result = 0
    for gift in gifts:
        result += gift.wrapping_paper()
    assert result == 1588178


def test_all_gifts_ribbon(gifts):
    assert len(gifts) == 1000
    result = 0
    for gift in gifts:
        result += gift.wrapping_ribbon()
    assert result == 3783758