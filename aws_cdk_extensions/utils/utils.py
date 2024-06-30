# list_utils.py

class ListUtils:

    @staticmethod
    def flatten_list(nested_list: list) -> list:
        """Flatten a nested list."""
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(ListUtils.flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

    @staticmethod
    def remove_duplicates(lst: list) -> list:
        """Remove duplicate items from the list."""
        return list(set(lst))

    @staticmethod
    def find_common_elements(list1: list, list2: list) -> list:
        """Find common elements between two lists."""
        return list(set(list1) & set(list2))
