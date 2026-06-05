#!/usr/bin/python3
"""
Log parsing module.

This script reads from standard input line by line, computes metrics
(total file size and status code counts), and prints statistics
every 10 lines or upon receiving a KeyboardInterrupt (CTRL+C).
"""
import sys


def print_stats(total_size, dict_status):
    """
    Print the accumulated metrics.

    Args:
        total_size (int): The total accumulated file size.
        dict_status (dict): Dictionary containing
        status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for key in sorted(dict_status.keys()):
        if dict_status[key] > 0:
            print("{}: {}".format(key, dict_status[key]))


if __name__ == "__main__":
    total_size = 0
    count = 0
    dict_status = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
        }

try:
    for line in sys.stdin:

        count += 1

        words = line.split()

        try:

            size = int(words[-1])
            total_size += size

            status = int(words[-2])
            if status in dict_status:
                dict_status[status] += 1
        except (ValueError, IndexError):
            pass

        if count == 10:
            print_stats(total_size, dict_status)
            count = 0

    print_stats(total_size, dict_status)

except KeyboardInterrupt:
    print_stats(total_size, dict_status)
    raise
