#!/usr/bin/python3
import sys

def print_stats(total_size, dict_status):
    print("File size: {}".format(total_size, dict_status))
    for key in sorted(dict_status.keys()):
        if dict_status[key] > 0:
            print("{}: {}".format(key, dict_status[key]))


if __name__ == "__main__":
    total_size = 0
    count = 0
    dict_status = {
            200:0,
            301:0,
            400:0,
            401:0,
            403:0,
            404:0,
            405:0,
            500:0,
        }
    try:
        for line in sys.stdin:
            words = line.strip().split(' ')
            try:
                size = int(words[-1])
                status = int(words[-2])
                total_size += size
                if status in dict_status:
                    count += 1
                    dict_status[status] += 1
            except (ValueError, IndexError):
                if count == 10:
                    print_stats(total_size, dict_status)
                    count = 0

    except KeyboardInterrupt:
        print_stats(total_size, dict_status)
        raise