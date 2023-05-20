from utils import arrs
# import pytest


# @pytest.mark.parametrize("array, index, default, expected", [
#     ([1, 2, 3], 1, "test", 2),
#     ([], 0, "test", "test")
# ])
# def test_get(array, index, default, expected):
#     assert arrs.get(array, index, default) == expected
def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    """Проверка с пустым массивом"""
    assert arrs.my_slice([], 0, 2) == []
    """Проверка если start<0 и end=None"""
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]
    """Проверка со start=0 и end=None"""
    assert arrs.my_slice([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    """Проверка если start < -len"""
    assert arrs.my_slice([1, 2, 3, 4, 5], -8, 2) == [1, 2]
