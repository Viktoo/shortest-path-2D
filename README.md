# Shortest Path 2D
Shortest path solutions for 2D arrays using Breadth-First Search (BFS) Algorithm and Dijkstra's Algorithm. Implemented in Python.

## Setup

On Mac/Linux:

`source venv/bin/activate`

On Windows:

`.\\venv\\Scripts\\activate`

## Usage

`python unw.py` runs Breadth-First Search Algorithm (on stage 1 by default). Unweighted graphs only.

`python w.py` runs Dijkstra's Algorithm (on stage 2 by default). Considers weighted edges.

CSV files:
 - Stage 1 - Original first stage (unweighted)
 - Stage 2 - Original second stage (weighted)
 - Stage 3 - Weighted edges with clear varying paths for testing.
 - tiny.csv - A small 3x3 matrix on which my first iteration of Dijkstra's was built testing on.

## BFS Algorithm

The Breadth-First Search Algorithm explores nodes in layers. Take a node and explore all of its neighbors. Then take all the nodes you've seen, and explore all their neighbors, then take all those nodes, and so on. Time complexity `O(V+E)`.

It's particularly useful for finding shortest path on an unweighted graph

## Dijkstra's Algorithm

This is one of the most important algorithms in graph theory for finding shortest path. It is similar to BFS as it's exploring the nodes, with added functionality of utilizing a priority queue with distances(weights). Because of this, the graph must only contain _non-negative edge weights_. Single Source Shortest Path (SSSP) with time complexity `O(E*Log(V))`.

Particularly useful for weighted graphs

This is the pen-and-paper version of Dijkstra's if ran against tiny.csv

<img src="https://public-demo-bucket.s3.amazonaws.com/demo/IMG_7669.jpg" width="40%">

## Optimization

The time complexity of Dijkstra's Algorithm gives it an advantage over BFS while expanding the functionality to include graphs with weighted edges. Dijkstra's can be used to replace BFS in this case.

This implementation of Dijkstra's is "lazy" meaning it lazily deletes outdated (key, value) pairs. The "eager" version uses an Indexed Priority Queue (IPQ) that avoids duplicate (key, value) pairs. It allows access to pairs in the queue at constant time and updates in log time (if binary heap).

We can potentially further optimize by changing the heap we're using. Indexed Binary Heap → D-ary Heap.

This use-case of an apartment/house is particularly well-suited for an algorithm that takes direction into account such as A*. In this context we know the position of the end node, but even if we didn't, gearing a search algorithm around doorways would offer very efficient traversal of the building.
