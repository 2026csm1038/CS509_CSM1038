# CS509 Laboratory Repository

## Repository Overview
This repository contains all **individual** assignments for CS509 (First-Year M.Tech CSE, 2026).

## Student Details
- **Name:** Vanshika Aggarwal
- **Entry Number:** CSM1038

## Language and Environment
- **Language:** C++
- **Compiler:** g++ (GCC) — version : g++ (Ubuntu 15.2.0-16ubuntu1) 15.2.0
- **Compilation flags:** `-O2 -std=c++17`
- **OS / Machine:** Ubuntu (VirtualBox)

## Directory Structure
```
CS509_CSM1038/
|-- README.md
|-- common_wrapper/
|   `-- wrapper.cpp
|-- assignment_01/
|   |-- src/
|   |   |-- gemm.h
|   |   |-- gemm.cpp
|   |   |-- csr.h
|   |   `-- csr.cpp
|   |-- driver/
|   |   |-- driver.cpp          
|   `-- tests/
|       |-- gemm_test_01.txt
|       |-- gemm_test_02.txt
|       |-- ... (gemm_test_30.txt)
|       `-- csr_test_XX.txt   
```

## Common Wrapper: Build and Usage
`common_wrapper/wrapper.cpp` is a menu-driven launcher with two options:
1. **GEMM (Simple + Blocking)** — prompts for a GEMM test-file path and runs `./assignment_01/driver/gemm_driver <file>`.
2. **CSR Conversion Test** — prompts for a CSR test-file path and runs `./assignment_01/tests/csr_test <file>`.

**Build:**
```bash
g++ -O2 -std=c++17 common_wrapper/wrapper.cpp -o wrapper
```

**Run:**
```bash
./wrapper
```
---

## Assignment 01 - GEMM (Simple + Blocking) and CSR Conversion

### Objective
Implement General Matrix Multiplication (GEMM) using a direct nested-loop (Simple) approach and a cache-blocked (Blocking) approach, and implement an adjacency-list-to-CSR conversion helper.

### Algorithm / Approach

- **Simple GEMM:** Standard triple nested-loop matrix multiplication.
- **Blocking GEMM:** Performs multiplication using cache-friendly block tiling.
- **chooseBlockSize():** Selects a block size automatically based on the smallest matrix dimension (maximum 64).
- **CSRconversion():** Converts an adjacency list into CSR representation (`row_ptr`, `col_ind`, `values`).

### Input Format
GEMM input file (space-separated values), one test case per file:
```
M K N
Matrix A (M × K)
Matrix B (K × N)

**Assumptions:**
- Values are read as `double`.
- Both GEMM implementations run on the exact same input file so their outputs and timings are directly comparable.
- Degenerate cases (a zero dimension, e.g. `0 3 3`) are accepted and simply produce an empty result along that dimension.

### Helper Functions / CSR Conversion
- `int chooseBlockSize(int M, int K, int N)` 
- `CSRGraph CSRconversion(const vector<vector<pair<int,double>>>& adjList, int V, int E)`

### File Structure
| File | Purpose |
|---|---|
| `src/gemm.h` / `src/gemm.cpp` | `Simple()`, `Blocking()`, `chooseBlockSize()` |
| `src/csr.h` / `src/csr.cpp` | `CSRGraph` struct and `CSRconversion()` helper |
| `driver/driver.cpp` | Reads a GEMM test file, runs Simple then Blocking, prints both result matrices and their execution times |
| `tests/gemm_test_XX.txt` | One GEMM test case per file (30 test files) |

### Compilation
```bash
g++ -O2 -std=c++17 assignment_01/driver/driver.cpp assignment_01/src/gemm.cpp -o assignment_01/driver/gemm_driver
```

### Execution
Directly:
```bash
./assignment_01/driver/gemm_driver assignment_01/tests/gemm_test_01.txt
```
Or via the common wrapper: run `./wrapper`, choose option `1`, and enter the test-file path when prompted.
The driver prints:
```
Algorithm: GEMM Simple
Result matrix:
...
Execution time: <value> ms

Algorithm: GEMM Blocking
Result matrix:
...
Execution time: <value> ms
```
If no file is given, or the file cannot be opened, the driver prints an error and exits with a non-zero status.

### Test Cases and Result Table

For every test, Simple and Blocking were run on the same input and their result matrices were verified to match; block size shown is the value chosen automatically by `chooseBlockSize()`.

| Test File | M K N | Simple Time (ms) | Blocking Time (ms) | Block Size | Status |
|---|---|---|---|---|---|
| gemm_test_01.txt | 0 3 3 | 0.001357 | 0.001263 | 8 | Pass |
| gemm_test_02.txt | 3 0 3 | 0.004039 | 0.003138 | 8 | Pass |
| gemm_test_03.txt | 1 1 1 | 0.002554 | 0.002285 | 8 | Pass |
| gemm_test_04.txt | 2 3 2 | 0.006296 | 0.006119 | 8 | Pass |
| gemm_test_05.txt | 5 5 5 | 0.022529 | 0.024679 | 8 | Pass |
| gemm_test_06.txt | 10 10 10 | 0.133199 | 0.166185 | 8 | Pass |
| gemm_test_07.txt | 3 7 2 | 0.011233 | 0.009686 | 8 | Pass |
| gemm_test_08.txt | 8 2 9 | 0.02804 | 0.032195 | 8 | Pass |
| gemm_test_09.txt | 8 8 8 | 0.072049 | 0.07768 | 8 | Pass |
| gemm_test_10.txt | 64 64 64 | 34.224 | 35.3466 | 64 | Pass |
| gemm_test_11.txt | 63 63 63 | 32.9237 | 34.8843 | 32 | Pass |
| gemm_test_12.txt | 65 65 65 | 36.9196 | 37.919 | 64 | Pass |
| gemm_test_13.txt | 100 100 100 | 137.609 | 161.789 | 64 | Pass |
| gemm_test_14.txt | 300 300 300 | 4098.68 | 4551.63 | 64 | Pass |
| gemm_test_15.txt | 500 500 500 | 17897.8 | 18681.5 | 64 | Pass |
| gemm_test_16.txt | 1 6 5 | 0.007134 | 0.007053 | 8 | Pass |
| gemm_test_17.txt | 5 6 1 | 0.008104 | 0.008214 | 8 | Pass |
| gemm_test_18.txt | 4 1 4 | 0.006971 | 0.017796 | 8 | Pass |
| gemm_test_19.txt | 6 6 6 | 0.036138 | 0.050277 | 8 | Pass |
| gemm_test_20.txt | 5 5 5 | 0.02111 | 0.022824 | 8 | Pass |
| gemm_test_21.txt | 200 4 4 | 0.618526 | 0.688776 | 8 | Pass |
| gemm_test_22.txt | 4 4 200 | 0.455923 | 0.630317 | 8 | Pass |
| gemm_test_23.txt | 6 300 6 | 1.97263 | 2.30622 | 8 | Pass |
| gemm_test_24.txt | 97 89 101 | 120.501 | 135.24 | 64 | Pass |
| gemm_test_25.txt | 6 6 6 | 0.033638 | 0.036078 | 8 | Pass |
| gemm_test_26.txt | 600 600 600 | 31210.1 | 31903.9 | 64 | Pass |
| gemm_test_27.txt | 700 700 700 | 50104.7 | 51504.8 | 64 | Pass |
| gemm_test_28.txt | 800 800 800 | 70892.1 | 75634 | 64 | Pass |
| gemm_test_29.txt | 600 800 1000 | 72339.7 | 71415.8 | 64 | Pass |
| gemm_test_30.txt | 1000 1000 1000 | — | — | 64 | Not completed (run pending / too slow to finish) |

*Note: For small matrices (up to roughly 10x10), Simple GEMM was often slightly faster than Blocking — the tiling overhead outweighs the cache-reuse benefit at that scale. The benefit of blocking becomes more visible starting around 200+ dimension, though it is inconsistent here since the reported times measure a single run rather than an average of several runs .*

### Complexity

| Function | Time | Space |
|----------|------|-------|
| Simple GEMM | O(MKN) | O(MN) |
| Blocking GEMM | O(MKN) | O(MN) |
| chooseBlockSize | O(log(min(M,K,N))) | O(1) |
| CSRconversion | O(V+E) | O(V+E) |

### References

1. https://en.wikipedia.org/wiki/Loop_nest_optimization
2. https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_(CSR,_CRS_or_Yale_format)
