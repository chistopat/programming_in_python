import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrapped():
        return json.dumps(func())
    return wrapped

# print(to_json.__name__)
#
# @to_json
# def get_data():
#   return {
#     'data': 42
#   }
#
# print(get_data.__name__)
# #
# # print(get_data())

