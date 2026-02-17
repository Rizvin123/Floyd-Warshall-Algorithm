# README #

### What is this repository for? ###

This repository contains two implementations of the Floyd–Warshall algorithm for computing shortest paths between all pairs of nodes in a weighted directed graph.

The algorithm is implemented in:

1) An iterative version using three nested loops.

2) A recursive version that simulates the same triple-loop logic without using loops.

The purpose of this repository is to:

1) Demonstrate equivalence between iterative and recursive approaches.

2) Compare performance characteristics of both implementations.

3) Provide unit tests to validate correctness.

4) Maintain code quality using PEP 8 and pylint standards.

Version: 0.1

### How do I get set up? ###

1) Clone the repository

git clone https://github.com/Rizvin123/Floyd-Warshall-Algorithm.git

2) Navigate to the project directory

cd <repo-dir>

3) Ensure Python 3.8 or later is installed:

python --version

### Running the scripts ###

1) To run the iterative implementation:

python src/iterative/iterative_floyd.py

2) To run the recursive implementation:

python src/recursion/recursive_floyd.py

3) To run the performance comparison:

python src/performance/performance_test.py

4) To execute the unit tests:

python -m unittest src/tests/unittests.py


### Requirements ### 

1) Python 3.8 or later

2) Standard library only (no external dependencies)

