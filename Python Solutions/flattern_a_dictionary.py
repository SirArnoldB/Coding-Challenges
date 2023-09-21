# Flatten a Dictionary
# A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

# Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

# If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

# If a certain key is empty, it should be excluded from the output (see e in the example below).

# Example:

# input:  dict = {
#             "Key1" : "1",
#             "Key2" : {
#                 "a" : "2",
#                 "b" : "3",
#                 "c" : {
#                     "d" : "3",
#                     "e" : {
#                         "" : "1"
#                     }
#                 }
#             }
#         }

# output: {
#             "Key1" : "1",
#             "Key2.a" : "2",
#             "Key2.b" : "3",
#             "Key2.c.d" : "3",
#             "Key2.c.e" : "1"
#         }
# Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

# Constraints:

# [time limit] 5000ms
# [input] Dictionary dict
# [output] Dictionary

# Solution: Recursion


def flatten_dictionary(dictionary: dict) -> dict:
    key_values = {}

    def flatten_value(dict_value: dict, key_path: list) -> None:
        for key, value in dict_value.items():
            new_key_path = key_path + [key] if key else key_path
            if isinstance(value, dict):
                flatten_value(value, new_key_path)
            else:
                key_values[".".join(new_key_path)] = value

    flatten_value(dictionary, [])

    return key_values


if __name__ == "__main__":
    dictionary = {
        "Key1": "1",
        "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": {"": "1"}}},
    }

    print(flatten_dictionary(dictionary))

# Time complexity: O(n) - we iterate through all the keys in the dictionary once and add them to the key_values dictionary in O(1) time (assuming the keys are strings)
# Space complexity: O(n) - we store n keys in the key_values dictionary and n recursive calls on the call stack (assuming the keys are strings)
