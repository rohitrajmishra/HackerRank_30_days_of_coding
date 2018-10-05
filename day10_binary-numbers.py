#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary_num = "{0:b}".format(n)
    # print(binary_num)
    count = 0
    count_list = []
    for i in binary_num:
        val = int(i)
        if val == 1:
            count += 1
            # print(count)
        else:
            # print(count_list)
            count = 0
        count_list.append(count)
    print(max(count_list))