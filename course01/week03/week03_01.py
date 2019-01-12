class FileReader:

    def __init__(self, filename=None):
        if not isinstance(filename, str):
            filename = None
        self._filename = filename

    def read(self):
        try:
            with open(self._filename, 'r') as _file_obj:
                result = _file_obj.read()
        except IOError:
            return ""
        else:
            return result


