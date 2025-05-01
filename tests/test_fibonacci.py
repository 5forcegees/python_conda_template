import fibonacci.fibonacci as fib
import pytest

def test_true_true():
    assert True == True

@pytest.mark.parametrize("value, expected",[
    (1,1),
    (2,1),
    (4,3),
    (13,233)
])
def test_fibonacci_five(value, expected):
    assert fib.f(value) == expected
