from fibonacci import FibonacciResource


def test_fibonacci_2():
    instance = FibonacciResource()
    assert instance.fibonacci(2) == [1, 1]


def test_fibonacci_eight():
    instance = FibonacciResource()
    assert instance.fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]
