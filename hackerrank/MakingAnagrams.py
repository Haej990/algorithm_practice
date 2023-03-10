#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    delete_count = 0
    
    # a and b are strings
    total_len = len(a) + len(b)
    
    a = list(a)
    b = list(b)
    
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                del(b[j])
                delete_count += 1
                break
    
    return total_len - 2 * delete_count
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
