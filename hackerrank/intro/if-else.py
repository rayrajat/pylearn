#!/bin/python3

import math
import os
import random
import re
import sys



def check_number(n):
    if (n%2!=0)or((n%2==0)and(6<n<=20)):
        return 'Weird'
    
    else:
        return 'Not Weird'
    

if __name__=="__main__":

    n = int(input())

    print(check_number(n))

