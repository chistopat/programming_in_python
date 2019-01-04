import json


def to_json(func):
    def wrapped():
        return json.dumps(func())
    return wrapped

# @to_json
# def get_data():
#   return {
#     'data': 42
#   }
#
# print(get_data())

