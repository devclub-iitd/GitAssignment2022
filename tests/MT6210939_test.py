def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

def test_answer():
    assert factorial(5) == 120

test_answer()