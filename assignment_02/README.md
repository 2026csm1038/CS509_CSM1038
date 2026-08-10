## Assignment 02 - Bellman-Ford and Floyd-Warshall

### Objective

Implement:

* **Bellman-Ford:** Single-source shortest path for a directed weighted graph with possible negative edge weights, including negative-cycle detection.
* **Floyd-Warshall:** All-pairs shortest path for a weighted graph represented using a dense distance matrix, including negative-cycle detection.

The Bellman-Ford implementation uses the common CSR graph representation for the graph input. Floyd-Warshall works directly on the dense matrix input and does not require CSR conversion.

### Algorithm / Approach

* **Bellman-Ford:** Initializes the source distance to zero and repeatedly relaxes all directed edges for up to `V - 1` iterations. An additional pass is used to detect a reachable negative-weight cycle.
* **Early Termination:** Bellman-Ford stops before `V - 1` iterations if no distance changes during a complete relaxation pass.
* **CSR Graph:** The input adjacency-list representation is converted into CSR using the common `CSRconversion()` helper before running Bellman-Ford.
* **Floyd-Warshall:** Uses three nested loops and considers every vertex as an intermediate vertex between every pair of vertices.
* **Floyd-Warshall Negative-Cycle Detection:** After the main computation, a negative cycle is detected if any diagonal entry `dist[i][i]` becomes negative.
* **Distance Type:** Bellman-Ford stores distances using `long double` to provide additional numerical precision and range when accumulating edge weights.

### Input Format

#### Bellman-Ford

The Bellman-Ford input file contains a directed weighted graph in adjacency-list form:

```text
V E
u degree v1 w1 v2 w2 ...
...
SOURCE s
```

Example:

```text
10 20
0 2 1 15 2 10
1 3 2 19 6 3 8 -8
2 4 3 -9 6 13 7 4 9 -7
...
SOURCE 0
```

Where:

* `V` = number of vertices.
* `E` = number of directed edges.
* `u` = source vertex of the adjacency-list row.
* `degree` = number of outgoing edges from vertex `u`.
* `vi` = destination vertex.
* `wi` = edge weight.
* `SOURCE s` specifies the source vertex.

Negative edge weights are allowed for Bellman-Ford. A separate test case is used for negative-cycle detection.

#### Floyd-Warshall

The Floyd-Warshall input file contains a dense `V × V` distance matrix:

```text
V
row 0
row 1
...
row V-1
```

Each matrix entry represents the direct edge weight between two vertices.

`INF` represents the absence of a direct edge.

The diagonal entries are initialized to `0`.

Example:

```text
5
0 3 8 INF -4
INF 0 INF 1 7
INF 4 0 INF INF
2 INF -5 0 INF
INF INF INF 6 0
```

### Helper Functions / CSR Conversion

#### Bellman-Ford

```cpp
BellmanFordResult bellmanFord(const CSRGraph &graph, int source)
```

The result contains:

```cpp
struct BellmanFordResult
{
    vector<long double> distance;
    bool hasNegativeCycle;
};
```

#### CSR Conversion

The common CSR helper is used for Bellman-Ford:

```cpp
CSRGraph CSRconversion(
    const vector<vector<pair<int,double>>>& adjList,
    int V,
    int E
);
```

The CSR graph stores:

* `row_ptr` — beginning/end positions of each vertex's outgoing edges.
* `col_ind` — destination vertices.
* `values` — edge weights.

CSR conversion is performed before the algorithm timing starts.

### File Structure

| File                                              | Purpose                                                                                         |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `src/bellman_ford.h` / `src/bellman_ford.cpp`     | Bellman-Ford algorithm and negative-cycle detection                                             |
| `src/floyd_warshall.h` / `src/floyd_warshall.cpp` | Floyd-Warshall algorithm and negative-cycle detection                                           |
| `driver/bellman_ford_driver.cpp`                  | Reads Bellman-Ford input, performs CSR conversion, runs Bellman-Ford and reports execution time |
| `driver/floyd_warshall_driver.cpp`                | Reads Floyd-Warshall matrix input, runs Floyd-Warshall and reports execution time               |
| `tests/bellman_ford/generate_bellman_ford.py`     | Generates Bellman-Ford graph test cases                                                         |
| `tests/bellman_ford/bf_*.txt`                     | Bellman-Ford test cases                                                                         |
| `tests/floyd_warshall/generate_floyd_warshall.py` | Generates Floyd-Warshall matrix test cases                                                      |
| `tests/floyd_warshall/fw_*.txt`                   | Floyd-Warshall test cases                                                                       |
| `../common/csr.h` / `../common/csr.cpp`           | Shared CSR graph representation and conversion helper                                           |

### Compilation

#### Bellman-Ford

From the repository root:

```bash
g++ -O2 -std=c++17 \
-Icommon \
-Iassignment_02/src \
common/csr.cpp \
assignment_02/src/bellman_ford.cpp \
assignment_02/driver/bellman_ford_driver.cpp \
-o bellman_ford_driver
```

#### Floyd-Warshall

From the repository root:

```bash
g++ -O2 -std=c++17 \
-Icommon \
-Iassignment_02/src \
assignment_02/src/floyd_warshall.cpp \
assignment_02/driver/floyd_warshall_driver.cpp \
-o floyd_warshall_driver
```

Floyd-Warshall does not require CSR conversion because its input is already a dense matrix.

### Execution

#### Bellman-Ford

```bash
./bellman_ford_driver assignment_02/tests/bellman_ford/bf_10.txt
```

Example output:

```text
Algorithm: Bellman-Ford
Source: 0
Vertex Distance
0 0.00
1 15.00
2 10.00
3 1.00
4 15.00
5 29.00
6 18.00
7 10.00
8 7.00
9 -1.00
Negative cycle: No
Execution time: 2 microseconds
```

For the negative-cycle test:

```bash
./bellman_ford_driver assignment_02/tests/bellman_ford/bf_negative_cycle.txt
```

Output:

```text
Algorithm: Bellman-Ford
Source: 0
Negative cycle: Yes
Execution time: 2 microseconds
```

#### Floyd-Warshall

```bash
./floyd_warshall_driver assignment_02/tests/floyd_warshall/fw_10.txt
```

The driver prints the shortest-distance matrix followed by the execution time.

For the negative-cycle test:

```bash
./floyd_warshall_driver assignment_02/tests/floyd_warshall/fw_negative_cycle.txt
```

Output:

```text
Negative weight cycle detected.

Execution Time : 0 ms
```

If no file is given, or the input file cannot be opened, the corresponding driver reports an error and exits with a non-zero status.

### Test Cases and Result Table

The test generators were used to create the required graph sizes.

#### Bellman-Ford Test Cases

| Test File               |       V |       E | Execution Time (µs) | Status |
| ----------------------- | ------: | ------: | ------------------: | ------ |
| `bf_10.txt`             |      10 |      20 |                   2 | Pass   |
| `bf_100.txt`            |     100 |     300 |                  17 | Pass   |
| `bf_10000.txt`          |  10,000 |  30,000 |               2,099 | Pass   |
| `bf_50000.txt`          |  50,000 | 150,000 |              12,720 | Pass   |
| `bf_100000.txt`         | 100,000 | 300,000 |              21,213 | Pass   |
| `bf_negative_cycle.txt` |      10 |      10 |                   2 | Pass   |

The Bellman-Ford test cases include negative edge weights in the normal graph tests. The dedicated negative-cycle test verifies that the implementation detects a negative-weight cycle.

#### Floyd-Warshall Test Cases

| Test File               |     V | Execution Time (ms) | Status |
| ----------------------- | ----: | ------------------: | ------ |
| `fw_10.txt`             |    10 |                   0 | Pass   |
| `fw_100.txt`            |   100 |                  30 | Pass   |
| `fw_500.txt`            |   500 |               1,829 | Pass   |
| `fw_1000.txt`           | 1,000 |              18,882 | Pass   |
| `fw_2000.txt`           | 2,000 |             190,898 | Pass   |
| `fw_negative_cycle.txt` |    10 |                   0 | Pass   |

The Floyd-Warshall test cases cover the required graph sizes and include a separate negative-cycle test.

*Note: The execution times above are from single runs on the Ubuntu VirtualBox environment. They can vary depending on system load and available resources. The small `fw_10` and negative-cycle tests report `0 ms` because their execution time is below the millisecond resolution currently used by the Floyd-Warshall driver.*

### Test Generators

#### Bellman-Ford

The Bellman-Ford test generator is:

```text
tests/bellman_ford/generate_bellman_ford.py
```

It generates graph sizes:

```text
V = 10
V = 100
V = 10,000
V = 50,000
V = 100,000
```

The generated large graphs remain sparse so that Bellman-Ford can be tested on larger vertex counts without constructing a dense graph.

A separate negative-cycle input is generated for checking negative-cycle detection.

#### Floyd-Warshall

The Floyd-Warshall test generator is:

```text
tests/floyd_warshall/generate_floyd_warshall.py
```

It generates:

```text
V = 10
V = 100
V = 500
V = 1,000
V = 2,000
```

A separate negative-cycle input is generated to verify negative-cycle detection.

### Complexity

| Function / Algorithm | Time     | Space    |
| -------------------- | -------- | -------- |
| Bellman-Ford         | O(VE)    | O(V)     |
| Floyd-Warshall       | O(V³)    | O(V²)    |
| CSRconversion        | O(V + E) | O(V + E) |

Bellman-Ford uses CSR for the graph representation, while Floyd-Warshall uses the dense distance matrix directly.

### Execution-Time Measurement

For Bellman-Ford, input reading and CSR conversion are completed before starting the algorithm timer. The measured section contains the Bellman-Ford relaxation process and negative-cycle detection.

For Floyd-Warshall, input reading and matrix construction are completed before the algorithm timer starts. The measured section contains the Floyd-Warshall computation and negative-cycle check.

This keeps input processing and preprocessing separate from the reported algorithm execution time.

### References

1. https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
2. https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
3. https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_(CSR,_CRS_or_Yale_format)

