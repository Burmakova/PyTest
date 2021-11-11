import pytest
from gifts import Gift


def test_all_gifts_paper(gifts):
    assert len(gifts) == 500
    result = 0
    for gift in gifts:
        result += gift.wrapping_paper()
    assert result == 790444


def test_all_gifts_ribbon(gifts):
    assert len(gifts) == 500
    result = 0
    for gift in gifts:
        result += gift.wrapping_ribbon()
    assert result == 1874570


class TestGifts:
    @pytest.fixture
    def gifts(self):
        # Using readlines()
        input_txt = open('input2.txt', 'r')
        Lines = input_txt.readlines()

        gifts = []
        # Strips the newline character
        for line in Lines:
            sizes = line.split('x')
            gifts.append(Gift(int(sizes[0]), int(sizes[1]), int(sizes[2])))
        return gifts

    def test_all_gifts_ribbon(self, gifts):
        assert len(gifts) == 500
        result = 0
        for gift in gifts:
            result += gift.wrapping_ribbon()
        assert result == 1909188