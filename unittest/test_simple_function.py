from simple_function import add
import pytest


@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (5, 5, 10),
    (6, 6, 12)
])
def test_add(x, y, result):
    assert add(x, y) == result

# run all test of folder .
if __name__ == '__main__':
    pytest.main(["-x", ".", "-vv"])
