#!/usr/bin/python3
"""
Module 0-validate_utf8 Contains a method to determine
if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Checks if a given data set represents a valid UTF-8 encoding."""
    num_octets = 0

    for octet in data:

        if num_octets > 0:
            if (octet >> 6) != 2:
                return False
            num_octets = num_octets - 1
        else:
            if (octet >> 5) == 6:
                num_octets = 1
            elif (octet >> 4) == 14:
                num_octets = 2
            elif (octet >> 3) == 30:
                num_octets = 3
            elif (octet >> 7) == 0:
                num_octets = 0
            else:
                return False

    return num_octets == 0
