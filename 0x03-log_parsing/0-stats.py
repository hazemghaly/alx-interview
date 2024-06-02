#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""


def parseLogs():
    """
    Reads logs from standard input and generates logsprints
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    size = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                size += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                logsprint(size, statusCodes)
                lineNumber = 0
        logsprint(size, statusCodes)
    except KeyboardInterrupt as e:
        logsprint(size, statusCodes)
        raise


def logsprint(size, statusCodes):
    """
    Prints generated logsprint to standard output
    """
    print("File size: {}".format(size))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
