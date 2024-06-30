# data_utils.py

class DataUtils:

    @staticmethod
    def merge_dicts(dict1: dict, dict2: dict) -> dict:
        """Merge two dictionaries into one. Values from the second dictionary override those from the first."""
        merged_dict = dict1.copy()
        merged_dict.update(dict2)
        return merged_dict

    @staticmethod
    def get_dict_keys(d: dict) -> list:
        """Return the list of keys from the dictionary."""
        return list(d.keys())

    @staticmethod
    def get_dict_values(d: dict) -> list:
        """Return the list of values from the dictionary."""
        return list(d.values())

    @staticmethod
    def find_largest(numbers: list) -> int:
        """Return the largest number in the list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        return max(numbers)

    @staticmethod
    def count_occurrences(s: str, char: str) -> int:
        """Count occurrences of a character in a string."""
        return s.count(char)
