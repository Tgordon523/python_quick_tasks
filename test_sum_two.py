from sum_two import sum_two_index


def test_example1():
    example1 = [2, 3, 5, 1]
    result1 = 3
    assert sum_two_index(example1, result1) == [0, 3]


def test_example2():
    example2 = [3, 2, 1, 4]
    result2 = 5
    assert sum_two_index(example2, result2) == [0, 1]
