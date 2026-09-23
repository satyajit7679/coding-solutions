#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    n = len(timestamps)

    if n == 0:
        return 0

    low = 0
    high = 1

    while high < n:
        if timestamps[high] - timestamps[low] < K:
            # Remove current element
            high += 1
        else:
            # Keep current element
            low += 1
            timestamps[low] = timestamps[high]
            high += 1

    return low + 1

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
