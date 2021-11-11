import pytest
from gifts import Gift


@pytest.fixture
def my_gift():
    return Gift(2, 3, 4)


@pytest.fixture
def gifts():
    # Using readlines()
    input_txt = open('input.txt', 'r')
    Lines = input_txt.readlines()

    gifts = []
    # Strips the newline character
    for line in Lines:
        sizes = line.split('x')
        gifts.append(Gift(int(sizes[0]), int(sizes[1]), int(sizes[2])))
    return gifts