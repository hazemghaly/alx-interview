#!/usr/bin/python3
"""interview """


def validUTF8(data):
    """check validtion
    """
    try:
        if any(not 0 <= byte <= 255 for byte in data):
            return False
        bytes_data = bytes(data)
        bytes_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
