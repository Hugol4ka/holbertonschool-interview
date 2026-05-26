#!/usr/bin/python3

def minOperations(n):
    """Calculate the minimum number of operation exactly n characteristics H"""
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
