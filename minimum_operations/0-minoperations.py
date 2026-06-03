#!/usr/bin/python3
"""
Module for calculating the minimum number of operation to achieve n characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters.
    """
    if n <= 1:
        return 0

    num_ops = 0
    div = 2
    while n > 1:
        while n % div == 0:
            num_ops = num_ops + div
            n //= div
        div = div + 1
    return num_ops
