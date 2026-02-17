"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
sys.path.append('../')
from recursion.recursive_floyd import main as recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd
from time import process_time

def performance_test(function_handle, repetitions=10000):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters

    """
    start_time = process_time()

    for _ in range(repetitions):
        function_handle()

    end_time = process_time()

    elapsed_time = end_time - start_time
    print("Time taken:", elapsed_time)
    

print ("Recursion Test Time")
performance_test(recursive_floyd_warshall)

print ("Iterative Test Time")
performance_test(iterative_floyd)

    


