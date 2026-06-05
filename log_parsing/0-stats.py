#!/usr/bin/python3
"""
Log parsing module.
"""
import sys


def print_stats(total_size, dict_status):
    """
    Print the accumulated metrics.
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

            if len(words) < 2:
                continue

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
