"""Unit tests for iterative and recursive Floyd-Warshall implementations."""

import copy
import os
import sys
import unittest

CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(SRC_DIR)

from recursion import recursive_floyd  
from iterative import iterative_floyd  


ORIGINAL_GRAPH = [
    [0, 7, recursive_floyd.NO_PATH, 8],
    [recursive_floyd.NO_PATH, 0, 5, recursive_floyd.NO_PATH],
    [recursive_floyd.NO_PATH, recursive_floyd.NO_PATH, 0, 2],
    [recursive_floyd.NO_PATH, recursive_floyd.NO_PATH,
     recursive_floyd.NO_PATH, 0],
]

EXPECTED_RESULT = [
    [0, 7, 12, 8],
    [recursive_floyd.NO_PATH, 0, 5, 7],
    [recursive_floyd.NO_PATH, recursive_floyd.NO_PATH, 0, 2],
    [recursive_floyd.NO_PATH, recursive_floyd.NO_PATH,
     recursive_floyd.NO_PATH, 0],
]


class TestFloydWarshall(unittest.TestCase):
    """Test suite for Floyd-Warshall implementations."""

    def setUp(self):
        """Reset graph before each test."""
        recursive_floyd.GRAPH = copy.deepcopy(ORIGINAL_GRAPH)
        iterative_floyd.GRAPH = copy.deepcopy(ORIGINAL_GRAPH)

    def test_iterative_floyd_correctness(self):
        """Iterative implementation produces expected result."""
        iterative_floyd.iterative_floyd()
        self.assertEqual(iterative_floyd.GRAPH, EXPECTED_RESULT)

    def test_recursive_floyd_correctness(self):
        """Recursive implementation produces expected result."""
        recursive_floyd.recursive_floyd_warshall(
            recursive_floyd.MIN_LEVEL,
            recursive_floyd.MIN_LEVEL,
            recursive_floyd.MIN_LEVEL,
        )
        self.assertEqual(recursive_floyd.GRAPH, EXPECTED_RESULT)

    def test_algorithms_produce_same_result(self):
        """Recursive and iterative implementations match."""
        recursive_floyd.recursive_floyd_warshall(
            recursive_floyd.MIN_LEVEL,
            recursive_floyd.MIN_LEVEL,
            recursive_floyd.MIN_LEVEL,
        )
        recursive_result = copy.deepcopy(recursive_floyd.GRAPH)

        iterative_floyd.GRAPH = copy.deepcopy(ORIGINAL_GRAPH)
        iterative_floyd.iterative_floyd()

        self.assertEqual(recursive_result, iterative_floyd.GRAPH)


if __name__ == "__main__":
    unittest.main()