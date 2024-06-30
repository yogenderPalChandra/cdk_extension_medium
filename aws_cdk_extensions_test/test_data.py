# data_utils.py

from aws_cdk_extensions.data.data_utils import DataUtils


def test_merge_dicts():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = DataUtils.merge_dicts(dict1, dict2)
    assert merged == {'a': 1, 'b': 3, 'c': 4}

def test_get_dict_keys():
    d = {'x': 10, 'y': 20}
    keys = DataUtils.get_dict_keys(d)
    assert keys == ['x', 'y']

def test_get_dict_values():
    d = {'x': 10, 'y': 20}
    values = DataUtils.get_dict_values(d)
    assert values == [10, 20]

def test_find_largest():
    assert DataUtils.find_largest([1, 2, 3]) == 3
    assert DataUtils.find_largest([-1, 0, 1]) == 1
    assert DataUtils.find_largest([10, 20, 30, 40]) == 40
    try:
        DataUtils.find_largest([])
    except ValueError as e:
        assert str(e) == "List cannot be empty"

def test_count_occurrences():
    assert DataUtils.count_occurrences("hello world", 'o') == 2
    assert DataUtils.count_occurrences("Python", 't') == 1
    assert DataUtils.count_occurrences("aaaa", 'a') == 4
    assert DataUtils.count_occurrences("test", 'x') == 0
