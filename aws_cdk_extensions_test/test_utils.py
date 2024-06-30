# test_list_utils.py

from aws_cdk_extensions.utils.utils import ListUtils

def test_flatten_list():
    assert ListUtils.flatten_list([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]

def test_remove_duplicates():
    assert ListUtils.remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

def test_find_common_elements():
    assert ListUtils.find_common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert ListUtils.find_common_elements([1, 2, 3], [4, 5, 6]) == []
