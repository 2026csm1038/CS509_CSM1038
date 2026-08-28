import os
import random

# ============================================================
# CS509 Lab 4
# Test Case Generator
#
# Algorithms:
#   1. Greedy Vertex Coloring
#   2. PageRank
#
# Vertex Coloring:
#   Undirected, unweighted graph
#   No self-loops
#   Each undirected edge appears in both adjacency lists
#
# PageRank:
#   Directed, unweighted graph
#   Outgoing edges only
#   Supports dangling vertices
#
# Required sizes:
#   Vertex Coloring: 10, 100, 10000, 50000, 100000
#   PageRank:        10, 100, 1000, 10000, 50000
# ============================================================

SEED = 509
random.seed(SEED)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COLOR_DIR = os.path.join(BASE_DIR, "vertex_coloring")
PR_DIR = os.path.join(BASE_DIR, "pagerank")

os.makedirs(COLOR_DIR, exist_ok=True)
os.makedirs(PR_DIR, exist_ok=True)


# ============================================================
# Common helper
# ============================================================

def write_text(path, text):
    with open(path, "w") as f:
        f.write(text)


# ============================================================
# VERTEX COLORING
# ============================================================

def write_undirected_graph(path, n, edges):
    """
    Write an undirected adjacency-list graph.

    Format:
        V E
        vertex degree neighbor1 neighbor2 ...

    Each undirected edge {u,v} appears in both adjacency lists.
    E counts each undirected edge only once.
    """

    adj = [[] for _ in range(n)]

    for u, v in edges:
        if u == v:
            continue

        adj[u].append(v)
        adj[v].append(u)

    for i in range(n):
        adj[i] = sorted(set(adj[i]))

    actual_edges = sum(len(x) for x in adj) // 2

    with open(path, "w") as f:
        f.write(f"{n} {actual_edges}\n")

        for u in range(n):
            f.write(
                f"{u} {len(adj[u])}"
                + ("" if not adj[u] else " " + " ".join(map(str, adj[u])))
                + "\n"
            )


def path_edges(n):
    return [(i, i + 1) for i in range(n - 1)]


def cycle_edges(n):
    edges = path_edges(n)

    if n > 2:
        edges.append((n - 1, 0))

    return edges


def star_edges(n):
    return [(0, i) for i in range(1, n)]


def complete_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def random_sparse_undirected_edges(n, target_edges):
    """
    Generate a sparse random graph.

    target_edges is normally between 2N and 4N
    for the large required graphs.
    """

    max_edges = n * (n - 1) // 2
    target_edges = min(target_edges, max_edges)

    edge_set = set()

    # First create a path so that the graph is connected.
    for i in range(n - 1):
        edge_set.add((i, i + 1))

    while len(edge_set) < target_edges:
        u = random.randrange(n)
        v = random.randrange(n)

        if u == v:
            continue

        if u > v:
            u, v = v, u

        edge_set.add((u, v))

    return list(edge_set)


def generate_coloring_required_tests():
    # --------------------------------------------------------
    # Required graph sizes
    # --------------------------------------------------------

    required = [
        (10, 20),
        (100, 200),
        (10000, 20000),
        (50000, 100000),
        (100000, 200000),
    ]

    for n, e in required:
        edges = random_sparse_undirected_edges(n, e)

        path = os.path.join(COLOR_DIR, f"color_{n}.txt")

        write_undirected_graph(path, n, edges)

        print(f"Created {path}")


def generate_coloring_edge_cases():
    """
    Additional small graphs for correctness and edge cases.
    """

    # 1. Single vertex
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_single_vertex.txt"),
        1,
        []
    )

    # 2. Two vertices, one edge
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_two_vertices.txt"),
        2,
        [(0, 1)]
    )

    # 3. Empty graph
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_empty.txt"),
        10,
        []
    )

    # 4. Path
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_path.txt"),
        10,
        path_edges(10)
    )

    # 5. Cycle
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_cycle.txt"),
        10,
        cycle_edges(10)
    )

    # 6. Star
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_star.txt"),
        10,
        star_edges(10)
    )

    # 7. Complete graph
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_complete_5.txt"),
        5,
        complete_edges(5)
    )

    # 8. Bipartite graph K3,3
    edges = []

    for u in range(3):
        for v in range(3, 6):
            edges.append((u, v))

    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_bipartite.txt"),
        6,
        edges
    )

    # 9. Two disconnected components
    edges = [
        (0, 1),
        (1, 2),
        (3, 4),
        (4, 5)
    ]

    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_disconnected.txt"),
        8,
        edges
    )

    # 10. Triangle
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_triangle.txt"),
        3,
        [(0, 1), (1, 2), (2, 0)]
    )

    # 11. Dense but not complete
    write_undirected_graph(
        os.path.join(COLOR_DIR, "color_dense_20.txt"),
        20,
        random_sparse_undirected_edges(20, 100)
    )


# ============================================================
# PAGERANK
# ============================================================

def write_directed_graph(path, n, edges,
                          damping=0.85,
                          tolerance=0.0001,
                          max_iterations=100):

    adj = [[] for _ in range(n)]

    for u, v in edges:
        if u == v:
            continue

        adj[u].append(v)

    for i in range(n):
        adj[i] = sorted(set(adj[i]))

    actual_edges = sum(len(x) for x in adj)

    with open(path, "w") as f:

        f.write(f"{n} {actual_edges}\n")

        for u in range(n):
            f.write(
                f"{u} {len(adj[u])}"
                + ("" if not adj[u] else " " + " ".join(map(str, adj[u])))
                + "\n"
            )

        f.write(f"DAMPING {damping}\n")
        f.write(f"TOLERANCE {tolerance}\n")
        f.write(f"MAX_ITERATIONS {max_iterations}\n")


def random_sparse_directed_edges(n, target_edges):
    """
    Generate a sparse directed graph.

    A directed cycle is first added so that every vertex
    participates in the graph. Additional random directed
    edges are then added.
    """

    max_edges = n * (n - 1)

    target_edges = min(target_edges, max_edges)

    edge_set = set()

    # Directed cycle.
    if n > 1:
        for i in range(n):
            edge_set.add((i, (i + 1) % n))

    while len(edge_set) < target_edges:

        u = random.randrange(n)
        v = random.randrange(n)

        if u == v:
            continue

        edge_set.add((u, v))

    return list(edge_set)


def generate_pagerank_required_tests():

    required = [
        (10, 20),
        (100, 200),
        (1000, 2000),
        (10000, 20000),
        (50000, 100000),
    ]

    for n, e in required:

        edges = random_sparse_directed_edges(n, e)

        path = os.path.join(PR_DIR, f"pagerank_{n}.txt")

        write_directed_graph(
            path,
            n,
            edges,
            damping=0.85,
            tolerance=0.0001,
            max_iterations=100
        )

        print(f"Created {path}")


def generate_pagerank_edge_cases():

    # --------------------------------------------------------
    # 1. Example from specification
    # --------------------------------------------------------

    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (3, 2)
    ]

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_example.txt"),
        4,
        edges,
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 2. Single vertex with dangling vertex
    # --------------------------------------------------------

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_single_vertex.txt"),
        1,
        [],
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 3. Two vertices
    # --------------------------------------------------------

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_two_vertices.txt"),
        2,
        [(0, 1), (1, 0)],
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 4. Simple directed chain
    #
    # Last vertex is dangling.
    # --------------------------------------------------------

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_chain.txt"),
        10,
        [(i, i + 1) for i in range(9)],
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 5. Directed cycle
    # --------------------------------------------------------

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_cycle.txt"),
        10,
        [(i, (i + 1) % 10) for i in range(10)],
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 6. Star-like directed graph
    # --------------------------------------------------------

    edges = []

    for i in range(1, 10):
        edges.append((0, i))

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_star.txt"),
        10,
        edges,
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 7. Several dangling vertices
    # --------------------------------------------------------

    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 3),
        (4, 3)
    ]

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_dangling.txt"),
        6,
        edges,
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 8. Multiple incoming links
    # --------------------------------------------------------

    edges = [
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 5),
        (5, 0)
    ]

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_high_incoming.txt"),
        6,
        edges,
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 9. Disconnected directed components
    # --------------------------------------------------------

    edges = [
        (0, 1),
        (1, 0),
        (2, 3),
        (3, 2),
        (4, 5),
        (5, 4)
    ]

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_disconnected.txt"),
        6,
        edges,
        damping=0.85,
        tolerance=0.0001,
        max_iterations=100
    )

    # --------------------------------------------------------
    # 10. Very strict tolerance
    # --------------------------------------------------------

    edges = [
        (0, 1),
        (1, 2),
        (2, 0)
    ]

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_strict_tolerance.txt"),
        3,
        edges,
        damping=0.85,
        tolerance=1e-12,
        max_iterations=1000
    )

    # --------------------------------------------------------
    # 11. Low maximum iterations
    #
    # Useful for checking:
    # Converged: false
    # --------------------------------------------------------

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_max_iterations.txt"),
        10,
        random_sparse_directed_edges(10, 20),
        damping=0.85,
        tolerance=1e-12,
        max_iterations=1
    )

    # --------------------------------------------------------
    # 12. Different valid damping factor
    # --------------------------------------------------------

    write_directed_graph(
        os.path.join(PR_DIR, "pagerank_damping_0_5.txt"),
        10,
        random_sparse_directed_edges(10, 20),
        damping=0.5,
        tolerance=0.0001,
        max_iterations=100
    )


# ============================================================
# Invalid input generators
#
# These are OPTIONAL and should be used to test driver
# validation/error handling, not normal algorithm execution.
# ============================================================

def generate_invalid_tests():

    invalid_color_dir = os.path.join(COLOR_DIR, "invalid")
    invalid_pr_dir = os.path.join(PR_DIR, "invalid")

    os.makedirs(invalid_color_dir, exist_ok=True)
    os.makedirs(invalid_pr_dir, exist_ok=True)

    # --------------------------------------------------------
    # Vertex Coloring: self-loop
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_color_dir, "color_self_loop.txt"),
        """3 2
0 2 0 1
1 1 0
2 0
"""
    )

    # --------------------------------------------------------
    # Vertex Coloring: out-of-range vertex
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_color_dir, "color_invalid_vertex.txt"),
        """3 1
0 1 5
1 1 0
2 0
"""
    )

    # --------------------------------------------------------
    # Vertex Coloring: mismatched degree
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_color_dir, "color_bad_degree.txt"),
        """3 2
0 2 1
1 1 0
2 0
"""
    )

    # --------------------------------------------------------
    # PageRank: damping = 0
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_pr_dir, "pagerank_bad_damping_zero.txt"),
        """3 2
0 1 1
1 1 2
2 0
DAMPING 0
TOLERANCE 0.0001
MAX_ITERATIONS 100
"""
    )

    # --------------------------------------------------------
    # PageRank: damping = 1
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_pr_dir, "pagerank_bad_damping_one.txt"),
        """3 2
0 1 1
1 1 2
2 0
DAMPING 1
TOLERANCE 0.0001
MAX_ITERATIONS 100
"""
    )

    # --------------------------------------------------------
    # PageRank: negative tolerance
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_pr_dir, "pagerank_bad_tolerance.txt"),
        """3 2
0 1 1
1 1 2
2 0
DAMPING 0.85
TOLERANCE -0.1
MAX_ITERATIONS 100
"""
    )

    # --------------------------------------------------------
    # PageRank: zero iterations
    # --------------------------------------------------------

    write_text(
        os.path.join(invalid_pr_dir, "pagerank_bad_iterations.txt"),
        """3 2
0 1 1
1 1 2
2 0
DAMPING 0.85
TOLERANCE 0.0001
MAX_ITERATIONS 0
"""
    )


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    print("==============================================")
    print("CS509 Lab 4 Test Generator")
    print("==============================================")

    print("\nGenerating required Vertex Coloring tests...")
    generate_coloring_required_tests()

    print("\nGenerating Vertex Coloring edge cases...")
    generate_coloring_edge_cases()

    print("\nGenerating required PageRank tests...")
    generate_pagerank_required_tests()

    print("\nGenerating PageRank edge cases...")
    generate_pagerank_edge_cases()

    print("\nGenerating invalid-input tests...")
    generate_invalid_tests()

    print("\n==============================================")
    print("All test cases generated successfully.")
    print("==============================================")
