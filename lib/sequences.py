#!/usr/bin/env python3

def get_fibonacci(number):
    return 


'''
start list with 0,1
for range of length/2-2 
get last 2 add up and append to list

'''
def print_fibonacci(length):
    if length == 0: 
        print([])
    elif length == 1:
        print([0])
    else: 
        fib_list = [0,1]
        for i in range(int(length-2)):
            fib_list.append(fib_list[-1] + fib_list[-2])
        print(fib_list)

print_fibonacci(8)