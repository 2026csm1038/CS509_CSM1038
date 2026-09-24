# CS509 – Assignment 4

## Individual Assignment: Greedy Vertex Coloring and PageRank

**Student:** Vanshika Aggarwal
**Entry Number:** CSM1038
**Language:** C++17
**Compiler:** g++
**Environment:** Ubuntu (VirtualBox)

## 1. Assignment Scope

This individual assignment implements two graph algorithms:

- Greedy Vertex Coloring
- PageRank

Both algorithms operate on graphs represented using CSR format.

## 2. Implementation Approach

### 2.1 Greedy Vertex Coloring

Greedy vertex coloring assigns the smallest available color to each vertex such that no two adjacent vertices have the same color.

**Time Complexity:** O(V + E)
**Space Complexity:** O(V + E)

### 2.2 PageRank

PageRank assigns an importance score to each vertex based on the ranks of vertices linking to it. The implementation uses iterative rank updates with a damping factor and handles dangling vertices.

**Time Complexity:** O(k(V + E)), where k is the number of iterations
**Space Complexity:** O(V + E)

## 3. Input Format

The graph input is provided in adjacency-list form and is converted to CSR before algorithm execution.

For PageRank, the input also contains the damping factor, tolerance and maximum iteration parameters as required by the assignment specification.

## 4. CSR Conversion and Timing

The input graph is converted to CSR using the common CSR helper.

CSR conversion, file reading and output printing are excluded from the measured algorithm time.

The timer starts immediately before the algorithm call and stops immediately after it finishes.

## 5. File Structure

assignment_04/
├── README.md
├── src/
│   ├── vertex_coloring.h
│   ├── vertex_coloring.cpp
│   ├── pagerank.h
│   └── pagerank.cpp
├── driver/
│   ├── vertex_coloring_driver.cpp
│   └── pagerank_driver.cpp
└── tests/
    ├── vertex_coloring/
    │   └── color_*.txt
    └── pagerank/
        └── pagerank_*.txt

## 6. Compilation

### Greedy Vertex Coloring

g++ -O2 -std=c++17 -Icommon -Iassignment_04/src common/csr.cpp assignment_04/src/vertex_coloring.cpp assignment_04/driver/vertex_coloring_driver.cpp -o assignment_04/driver/vertex_coloring_driver

### PageRank

g++ -O2 -std=c++17 -Icommon -Iassignment_04/src common/csr.cpp assignment_04/src/pagerank.cpp assignment_04/driver/pagerank_driver.cpp -o assignment_04/driver/pagerank_driver

## 7. Execution

### Greedy Vertex Coloring

./assignment_04/driver/vertex_coloring_driver assignment_04/tests/vertex_coloring/color.txt

### PageRank

./assignment_04/driver/pagerank_driver assignment_04/tests/pagerank/pagerank_example.txt

## 8. Test Cases and Results

### 8.1 Greedy Vertex Coloring Results Table

File | V | E | Colors Used | Valid? | Time | Status
color_100000.txt | 100000 | 200000 | 6 | Yes | 22.4217 ms | Pass
color_10000.txt | 10000 | 20000 | 5 | Yes | 1.35345 ms | Pass
color_100.txt | 100 | 200 | 4 | Yes | 0.013557 ms | Pass
color_10.txt | 10 | 20 | 4 | Yes | 0.001962 ms | Pass
color_50000.txt | 50000 | 100000 | 6 | Yes | 15.5905 ms | Pass
color_bipartite.txt | 6 | 9 | 2 | Yes | 0.001705 ms | Pass
color_complete_5.txt | 5 | 10 | 5 | Yes | 0.001514 ms | Pass
color_cycle.txt | 10 | 10 | 2 | Yes | 0.003164 ms | Pass
color_dense_20.txt | 20 | 100 | 8 | Yes | 0.006286 ms | Pass
color_disconnected.txt | 8 | 4 | 2 | Yes | 0.001164 ms | Pass
color_empty.txt | 10 | 0 | 1 | Yes | 0.00337 ms | Pass
color_path.txt | 10 | 9 | 2 | Yes | 0.002116 ms | Pass
color_single_vertex.txt | 1 | 0 | 1 | Yes | 0.003076 ms | Pass
color_star.txt | 10 | 9 | 2 | Yes | 0.002137 ms | Pass
color_triangle.txt | 3 | 3 | 3 | Yes | 0.001441 ms | Pass
color_two_vertices.txt | 2 | 1 | 2 | Yes | 0.034823 ms | Pass

### 8.2 PageRank Results Table

File | V | E | Damping | Top Vertex | Sum of Ranks | Iter. / Time | Status
pagerank_10000.txt | 10000 | 20000 | 0.85 | 1 | 1.0000000000 | 100 / 10.3994740000 ms | Pass
pagerank_1000.txt | 1000 | 2000 | 0.85 | 2 | 1.0000000000 | 100 / 0.9426090000 ms | Pass
pagerank_100.txt | 100 | 200 | 0.85 | 1 | 1.0000000000 | 100 / 0.0822100000 ms | Pass
pagerank_10.txt | 10 | 20 | 0.85 | 2 | 1.0000000000 | 100 / 0.0071520000 ms | Pass
pagerank_50000.txt | 50000 | 100000 | 0.85 | 1 | 1.0000000000 | 100 / 49.1118810000 ms | Pass
pagerank_chain.txt | 10 | 9 | 0.85 | 1 | 1.0000000000 | 100 / 0.0071970000 ms | Pass
pagerank_cycle.txt | 10 | 10 | 0.85 | 1 | 1.0000000000 | 100 / 0.0064000000 ms | Pass
pagerank_damping_0_5.txt | 10 | 20 | 0.5 | 2 | 1.0000000000 | 100 / 0.0045140000 ms | Pass
pagerank_dangling.txt | 6 | 5 | 0.85 | 1 | 1.0000000000 | 100 / 0.0050410000 ms | Pass
pagerank_disconnected.txt | 6 | 6 | 0.85 | 1 | 1.0000000000 | 100 / 0.0071860000 ms | Pass
pagerank_example.txt | 4 | 5 | 0.85 | 1 | 1.0000000000 | 100 / 0.0024460000 ms | Pass
pagerank_high_incoming.txt | 6 | 6 | 0.85 | 1 | 1.0000000000 | 100 / 0.0039370000 ms | Pass
pagerank_max_iterations.txt | 10 | 20 | 0.85 | 2 | 1.0000000000 | 1 / 0.0021880000 ms | Fail
pagerank_single_vertex.txt | 1 | 0 | 0.85 | 0 | 1.0000000000 | 100 / 0.0017360000 ms | Pass
pagerank_star.txt | 10 | 9 | 0.85 | 0 | 1.0000000000 | 100 / 0.0268910000 ms | Pass
pagerank_strict_tolerance.txt | 3 | 3 | 0.85 | 1 | 1.0000000000 | 1000 / 0.0047290000 ms | Pass
pagerank_two_vertices.txt | 2 | 2 | 0.85 | 1 | 1.0000000000 | 100 / 0.0019400000 ms | Pass

## 9. Test Observations

All Greedy Vertex Coloring test cases completed successfully. The test suite includes large sparse graphs, complete graphs, cycles, paths, stars, bipartite graphs, dense graphs, disconnected graphs, empty graphs, triangles and small boundary cases.

The PageRank test suite includes different graph sizes, chains, cycles, dangling vertices, disconnected graphs, different damping factors, high-incoming-degree vertices, star graphs, a single vertex, two vertices, strict tolerance and maximum-iteration cases.

The PageRank maximum-iteration test reached the specified iteration limit before satisfying the convergence condition and was therefore reported as Fail.

## 10. Correctness

For Greedy Vertex Coloring, correctness was checked by verifying that adjacent vertices have different colors.

For PageRank, correctness was checked by verifying that the rank values form a normalized distribution and by checking the reported top-ranked vertex and iteration behaviour.

## 11. Complexity Analysis

Algorithm | Time Complexity | Space Complexity
Greedy Vertex Coloring | O(V + E) | O(V + E)
PageRank | O(k(V + E)) | O(V + E)

Here, k represents the number of PageRank iterations.

## 12. Execution Environment

Language: C++17
Compiler: g++ (GCC) — Ubuntu 15.2.0-16ubuntu1
Compilation Flags: -O2 -std=c++17
OS / Machine: Ubuntu running in VirtualBox
Timing Method: std::chrono::high_resolution_clock
Reported Unit: milliseconds (ms)

## References

1. T. H. Cormen et al., Introduction to Algorithms, 4th Edition, MIT Press.
2. PageRank and link-analysis concepts.

