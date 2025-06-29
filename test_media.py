import pytest
from media import media

@pytest.mark.parametrize("a,b,c,expected", [
    (0, 0, 0, 0.0),
    (1, 2, 3, 2.0),
    (-1, 1, 0, 0.0),
    (2.5, 3.5, 4.0, pytest.approx(3.3333333)),
])
def test_media_valores(a, b, c, expected):
    assert media(a, b, c) == expected

def test_media_float_int():
    assert media(1, 2.5, 3) == pytest.approx(2.1666667)
