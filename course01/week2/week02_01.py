import os
import tempfile
import argparse
import json


def write_value(key, value, data=None):
    if not data:
        data = {}
    if key not in data.keys():
        data[key] = value
    else:
        data[key] += (', ' + value)
    return data


def search_value(key, data):
    if key in data.keys():
        return data[key]
    else:
        return None


def validate_file(data):
    try:
        return json.loads(data)
    except Exception as err:
        return {}


def create_parser():
    parser = argparse.ArgumentParser(description='Coursera Python programming task. File key storage')
    parser.add_argument('-k', '--key', required=True)
    parser.add_argument('-v', '--val')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    open(storage_path, 'a').close()

    with open(storage_path, mode='r') as storage_file:
        # print("Storage file is:", storage_path)
        storage_raw = storage_file.read()
        storage_data = validate_file(storage_raw)

    if not args.val:
        print(search_value(args.key, storage_data))
    else:
        with open(storage_path, 'w') as storage_file:
            storage_file.write(json.dumps(write_value(args.key, args.val, storage_data)))
            # print("New pair key/value successfully written")

