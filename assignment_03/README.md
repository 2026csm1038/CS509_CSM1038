# CS509 – Assignment 3

## Individual Assignment: Minimum Spanning Tree

**Student:** Vanshika Aggarwal  
**Entry Number:** CSM1038  
**Language:** C++17  
**Compiler:** g++  
**Environment:** Ubuntu (VirtualBox)

## 1. Assignment Scope

This individual assignment implements two Minimum Spanning Tree algorithms:

- Kruskal's Algorithm
- Prim's Algorithm

Both algorithms operate on the same weighted, undirected graph. The graph is converted from adjacency-list format to CSR format before the algorithm execution.

The two algorithms must produce the same minimum total MST weight. For graphs having multiple valid MSTs, the selected edges may differ.

## 2. Implementation Approach

### 2.1 Kruskal's Algorithm

Kruskal's algorithm sorts the graph edges by increasing weight and uses a Disjoint Set Union (DSU) structure to avoid cycles.

**Time Complexity:** O(E log E)  
**Space Complexity:** O(V + E)

### 2.2 Prim's Algorithm

Prim's algorithm starts from vertex 0 and repeatedly selects the minimum-weight edge connecting the current MST to an unvisited vertex.

**Time Complexity:** O(E log V)  
**Space Complexity:** O(V + E)

## 3. Input Format

The MST input is a weighted undirected adjacency-list:

V E
u0 degree neighbor weight ...
u1 degree neighbor weight ...
...
u(V-1) degree neighbor weight ...

Each undirected edge appears in the adjacency list of both endpoints and is counted once in E.

MST edge weights may be positive, zero, or negative. 

## 4. CSR Conversion and Timing

The adjacency-list input is converted to CSR using the common CSR helper.

CSR conversion, file reading and output printing are excluded from the measured algorithm time.

The timer starts immediately before the MST algorithm call and stops immediately after it finishes. 


## 5. File Structure

```text
assignment_03/
├── README.md
├── src/
│   ├── mst.h
│   └── mst.cpp
├── driver/
│   └── mst_driver.cpp
└── tests/
    ├── mst_*.txt
    └── generate_mst_tests.py
```
## 6. Compilation

The MST driver can be compiled using:

```bash
g++ -O2 -std=c++17 \
-Icommon \
-Iassignment_03/src \
common/csr.cpp \
assignment_03/src/mst.cpp \
assignment_03/driver/mst_driver.cpp \
-o assignment_03/driver/mst_driver

```

## 7. Test Cases and Results

| Test | V | E | Graph Type | Prim (us) | Kruskal (us) | Status |
|---|---:|---:|---|---:|---:|---|
| mst_bridge.txt | 6 | 7 | Bridge | 3 | 3 | Pass |
| mst_complete_20.txt | 20 | 190 | Complete | 41 | 36 | Pass |
| mst_complete_5.txt | 5 | 10 | Complete | 3 | 3 | Pass |
| mst_cycle_100.txt | 100 | 100 | Cycle | 27 | 27 | Pass |
| mst_cycle_5.txt | 5 | 5 | Cycle | 4 | 3 | Pass |
| mst_disconnected.txt | 6 | 4 | Disconnected | 2 | 3 | Disconnected |
| mst_duplicate_edges.txt | 4 | 7 | General | 3 | 4 | Pass |
| mst_equal_weights.txt | 5 | 7 | General | 3 | 4 | Pass |
| mst_heavy_edge.txt | 5 | 5 | General | 2 | 3 | Pass |
| mst_isolated_vertex.txt | 5 | 3 | Disconnected | 2 | 2 | Disconnected |
| mst_many_components.txt | 8 | 4 | Disconnected | 1 | 3 | Disconnected |
| mst_multiple_answers.txt | 4 | 6 | General | 3 | 3 | Pass |
| mst_negative_heavy.txt | 4 | 6 | General | 2 | 3 | Pass |
| mst_negative_weights.txt | 5 | 6 | General | 3 | 5 | Pass |
| mst_parallel_equal.txt | 3 | 5 | General | 2 | 2 | Pass |
| mst_path_100.txt | 100 | 99 | Path | 20 | 28 | Pass |
| mst_path_5.txt | 5 | 4 | Path | 2 | 3 | Pass |
| mst_random_1000.txt | 1000 | 2999 | Random | 1515 | 1317 | Pass |
| mst_random_100.txt | 100 | 299 | Random | 140 | 126 | Pass |
| mst_random_10.txt | 10 | 24 | Random | 6 | 6 | Pass |
| mst_random_5000.txt | 5000 | 14999 | Random | 9655 | 7188 | Pass |
| mst_random_disconnected_100.txt | 100 | 165 | Disconnected | 7 | 60 | Disconnected |
| mst_random_disconnected_20.txt | 20 | 24 | Disconnected | 3 | 7 | Disconnected |
| mst_self_loops.txt | 4 | 6 | General | 2 | 3 | Pass |
| mst_single_vertex.txt | 1 | 0 | Single Vertex | 0 | 0 | Pass |
| mst_star_1000.txt | 1000 | 999 | Star | 407 | 340 | Pass |
| mst_star_10.txt | 10 | 9 | Star | 4 | 4 | Pass |
| mst_test_01.txt | 5 | 6 | General | 2 | 2 | Pass |
| mst_two_vertices.txt | 2 | 1 | Two Vertices | 1 | 2 | Pass |
| mst_unique.txt | 5 | 7 | General | 3 | 3 | Pass |
| mst_zero_weight.txt | 4 | 4 | General | 2 | 2 | Pass |

## References

T. H. Cormen et al., *Introduction to Algorithms*, 4th Edition, MIT Press — Minimum Spanning Trees, Kruskal's Algorithm, and Prim's Algorithm.


