# CS509 Laboratory Repository

This repository contains the individual assignment for **CS509 (First-Year M.Tech CSE, 2026)**.

## Student Details

* **Name:** Vanshika Aggarwal
* **Entry Number:** CSM1038

## Language and Environment

* **Language:** C++
* **Compiler:** g++ (GCC) — Ubuntu 15.2.0-16ubuntu1
* **Compilation flags:** `-O2 -std=c++17`
* **OS / Machine:** Ubuntu running in VirtualBox

## Repository Structure

```text
CS509_CSM1038/
├── README.md
├── common/
│   ├── csr.h
│   └── csr.cpp
├── common_wrapper/
│   └── wrapper.cpp
├── assignment_01/
│   ├── README.md
│   ├── src/
│   ├── driver/
│   └── tests/
└── assignment_02/
    ├── README.md
    ├── src/
    ├── driver/
    └── tests/
```

## Common Components

### CSR Conversion

The CSR conversion helper is maintained in the common directory because it is reused by CSR-based assignments.

```text
common/
├── csr.h
└── csr.cpp
```

The helper converts an adjacency-list representation into Compressed Sparse Row (CSR) format using:

* `row_ptr`
* `col_ind`
* `values`

The Assignment 2 specification requires CSR conversion to be performed as preprocessing and its execution time excluded from the algorithm timing.

### Common Wrapper

The common wrapper provides a menu-driven way to launch assignment drivers.

The repository provides a Makefile to compile the common wrapper and the assignment drivers.

```text
make clean 
make 
./wrapper
```


## Assignments

### Assignment 01 — GEMM and CSR

Assignment 01 contains:

* Simple GEMM
* Blocking GEMM
* CSR conversion

Detailed implementation, testing, compilation and performance information is documented in:

```text
assignment_01/README.md
```

### Assignment 02 — Individual Graph Algorithms

Assignment 02 contains:

* Bellman-Ford
* Floyd-Warshall
* Test generators
* Required test cases

Detailed implementation, input formats, testing and performance information is documented in:

```text
assignment_02/README.md
```

## Build Environment

All C++ programs are compiled using:

```bash
g++ -O2 -std=c++17
```

Individual assignment READMEs contain the exact compilation and execution commands for their respective programs.

