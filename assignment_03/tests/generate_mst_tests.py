import random
from pathlib import Path


OUTPUT_DIR = Path("assignment_03/tests/mst")


def write_graph(filename, vertices, edges):
    """
    Write an undirected weighted graph.

    Input format:
        V E
        u v weight
        ...

    Each undirected edge is written only once because
    mst_driver.cpp adds both directions.
    """

    output_file = OUTPUT_DIR / filename

    with output_file.open("w") as file:
        file.write(f"{vertices} {len(edges)}\n")

        for u, v, weight in edges:
            file.write(f"{u} {v} {weight}\n")

    print(
        f"Generated {filename}: "
        f"V={vertices}, E={len(edges)}"
    )


def add_edge(edges, u, v, weight):
    edges.append((u, v, weight))


# ------------------------------------------------------------
# Basic edge cases
# ------------------------------------------------------------

def generate_single_vertex():
    write_graph(
        "mst_single_vertex.txt",
        1,
        []
    )


def generate_two_vertices():
    write_graph(
        "mst_two_vertices.txt",
        2,
        [(0, 1, 10)]
    )


def generate_zero_weight():
    write_graph(
        "mst_zero_weight.txt",
        4,
        [
            (0, 1, 0),
            (1, 2, 0),
            (2, 3, 5),
            (0, 3, 10)
        ]
    )


def generate_negative_weights():
    write_graph(
        "mst_negative_weights.txt",
        5,
        [
            (0, 1, -5),
            (0, 2, 2),
            (1, 2, -3),
            (1, 3, 4),
            (2, 4, -2),
            (3, 4, 1)
        ]
    )


def generate_all_equal_weights():
    write_graph(
        "mst_equal_weights.txt",
        5,
        [
            (0, 1, 7),
            (0, 2, 7),
            (1, 2, 7),
            (1, 3, 7),
            (2, 3, 7),
            (2, 4, 7),
            (3, 4, 7)
        ]
    )


# ------------------------------------------------------------
# Standard graph structures
# ------------------------------------------------------------

def generate_path(n, filename):
    edges = []

    for i in range(n - 1):
        add_edge(edges, i, i + 1, i + 1)

    write_graph(filename, n, edges)


def generate_cycle(n, filename):
    edges = []

    for i in range(n):
        add_edge(edges, i, (i + 1) % n, i + 1)

    write_graph(filename, n, edges)


def generate_star(n, filename):
    edges = []

    for i in range(1, n):
        add_edge(edges, 0, i, i)

    write_graph(filename, n, edges)


def generate_complete(n, filename):
    edges = []

    weight = 1

    for u in range(n):
        for v in range(u + 1, n):
            add_edge(edges, u, v, weight)
            weight += 1

    write_graph(filename, n, edges)


# ------------------------------------------------------------
# Graphs specifically designed for MST behaviour
# ------------------------------------------------------------

def generate_unique_mst():
    """
    Every edge has a different weight.
    This gives a unique MST.
    """

    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 3, 3),
        (3, 4, 4),
        (0, 4, 20),
        (0, 2, 15),
        (1, 3, 18)
    ]

    write_graph(
        "mst_unique.txt",
        5,
        edges
    )


def generate_multiple_msts():
    """
    Several MSTs are possible because many edges
    have the same weight.
    """

    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 3, 1),
        (3, 0, 1),
        (0, 2, 1),
        (1, 3, 1)
    ]

    write_graph(
        "mst_multiple_answers.txt",
        4,
        edges
    )


def generate_bridge():
    """
    Two dense regions connected by one bridge.
    The bridge must be present in the MST.
    """

    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (0, 2, 3),

        (3, 4, 1),
        (4, 5, 2),
        (3, 5, 3),

        (2, 3, 100)
    ]

    write_graph(
        "mst_bridge.txt",
        6,
        edges
    )


def generate_heavy_cycle():
    """
    One very heavy edge in a cycle should be excluded
    from the MST.
    """

    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 3, 3),
        (3, 4, 4),
        (4, 0, 100)
    ]

    write_graph(
        "mst_heavy_edge.txt",
        5,
        edges
    )


def generate_negative_cycle_graph():
    """
    Negative weights are allowed for MST.
    There is no concept of a negative cycle affecting
    MST correctness.
    """

    edges = [
        (0, 1, -10),
        (1, 2, -20),
        (2, 3, -5),
        (3, 0, 8),
        (0, 2, 2),
        (1, 3, 4)
    ]

    write_graph(
        "mst_negative_heavy.txt",
        4,
        edges
    )


# ------------------------------------------------------------
# Duplicate / parallel edge cases
# ------------------------------------------------------------

def generate_duplicate_edges():
    """
    Same pair of vertices appears multiple times
    with different weights.
    """

    edges = [
        (0, 1, 10),
        (0, 1, 2),
        (0, 1, 8),

        (1, 2, 5),
        (1, 2, 1),

        (2, 3, 4),
        (0, 3, 20)
    ]

    write_graph(
        "mst_duplicate_edges.txt",
        4,
        edges
    )


def generate_parallel_equal_edges():
    edges = [
        (0, 1, 5),
        (0, 1, 5),
        (1, 2, 5),
        (1, 2, 5),
        (0, 2, 5)
    ]

    write_graph(
        "mst_parallel_equal.txt",
        3,
        edges
    )


# ------------------------------------------------------------
# Self-loop cases
# ------------------------------------------------------------

def generate_self_loops():
    """
    Self-loops cannot be part of an MST.
    """

    edges = [
        (0, 0, -100),
        (1, 1, 1),
        (2, 2, -50),
        (0, 1, 4),
        (1, 2, 3),
        (2, 3, 2)
    ]

    write_graph(
        "mst_self_loops.txt",
        4,
        edges
    )


# ------------------------------------------------------------
# Disconnected graphs
# ------------------------------------------------------------

def generate_disconnected():
    edges = [
        (0, 1, 2),
        (1, 2, 3),

        (3, 4, 1),
        (4, 5, 2)
    ]

    write_graph(
        "mst_disconnected.txt",
        6,
        edges
    )


def generate_many_components():
    edges = [
        (0, 1, 1),
        (2, 3, 2),
        (4, 5, 3),
        (6, 7, 4)
    ]

    write_graph(
        "mst_many_components.txt",
        8,
        edges
    )


def generate_isolated_vertex():
    edges = [
        (0, 1, 2),
        (1, 2, 3),
        (2, 3, 4)
    ]

    write_graph(
        "mst_isolated_vertex.txt",
        5,
        edges
    )


# ------------------------------------------------------------
# Random connected graph
# ------------------------------------------------------------

def generate_random_connected(
    vertices,
    extra_edges,
    filename,
    seed
):
    random.seed(seed)

    edges = []
    used = set()

    # First create a random spanning tree.
    for v in range(1, vertices):
        parent = random.randint(0, v - 1)

        u = min(parent, v)
        w = max(parent, v)

        if (u, w) not in used:
            used.add((u, w))

            weight = random.randint(-20, 50)

            add_edge(
                edges,
                u,
                w,
                weight
            )

    # Add extra random edges.
    attempts = 0

    while len(edges) < vertices - 1 + extra_edges:
        u = random.randrange(vertices)
        v = random.randrange(vertices)

        if u == v:
            attempts += 1
            continue

        a = min(u, v)
        b = max(u, v)

        if (a, b) in used:
            attempts += 1

            if attempts > vertices * vertices * 5:
                break

            continue

        used.add((a, b))

        weight = random.randint(-20, 50)

        add_edge(
            edges,
            a,
            b,
            weight
        )

    write_graph(
        filename,
        vertices,
        edges
    )


# ------------------------------------------------------------
# Random disconnected graph
# ------------------------------------------------------------

def generate_random_disconnected(
    vertices,
    components,
    filename,
    seed
):
    random.seed(seed)

    if components >= vertices:
        raise ValueError(
            "Number of components must be smaller "
            "than number of vertices."
        )

    edges = []
    used = set()

    # Divide vertices into components.
    component_id = []

    base = vertices // components
    remainder = vertices % components

    current = 0

    for c in range(components):
        size = base

        if c < remainder:
            size += 1

        vertices_in_component = list(
            range(current, current + size)
        )

        current += size

        # Connect each component internally with a tree.
        for i in range(1, len(vertices_in_component)):
            v = vertices_in_component[i]

            parent_index = random.randrange(i)
            u = vertices_in_component[parent_index]

            a = min(u, v)
            b = max(u, v)

            if (a, b) not in used:
                used.add((a, b))

                add_edge(
                    edges,
                    a,
                    b,
                    random.randint(-10, 30)
                )

        # Add a few additional internal edges.
        for _ in range(len(vertices_in_component)):
            if len(vertices_in_component) < 2:
                break

            u, v = random.sample(
                vertices_in_component,
                2
            )

            a = min(u, v)
            b = max(u, v)

            if (a, b) not in used:
                used.add((a, b))

                add_edge(
                    edges,
                    a,
                    b,
                    random.randint(-10, 30)
                )

    write_graph(
        filename,
        vertices,
        edges
    )


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Basic cases
    generate_single_vertex()
    generate_two_vertices()
    generate_zero_weight()
    generate_negative_weights()
    generate_all_equal_weights()

    # Standard structures
    generate_path(
        5,
        "mst_path_5.txt"
    )

    generate_path(
        100,
        "mst_path_100.txt"
    )

    generate_cycle(
        5,
        "mst_cycle_5.txt"
    )

    generate_cycle(
        100,
        "mst_cycle_100.txt"
    )

    generate_star(
        10,
        "mst_star_10.txt"
    )

    generate_star(
        1000,
        "mst_star_1000.txt"
    )

    generate_complete(
        5,
        "mst_complete_5.txt"
    )

    generate_complete(
        20,
        "mst_complete_20.txt"
    )

    # MST-specific cases
    generate_unique_mst()
    generate_multiple_msts()
    generate_bridge()
    generate_heavy_cycle()
    generate_negative_cycle_graph()

    # Duplicate / self-loop cases
    generate_duplicate_edges()
    generate_parallel_equal_edges()
    generate_self_loops()

    # Disconnected cases
    generate_disconnected()
    generate_many_components()
    generate_isolated_vertex()

    # Random connected graphs
    generate_random_connected(
        10,
        15,
        "mst_random_10.txt",
        3001
    )

    generate_random_connected(
        100,
        200,
        "mst_random_100.txt",
        3002
    )

    generate_random_connected(
        1000,
        2000,
        "mst_random_1000.txt",
        3003
    )

    generate_random_connected(
        5000,
        10000,
        "mst_random_5000.txt",
        3004
    )

    # Random disconnected graphs
    generate_random_disconnected(
        20,
        4,
        "mst_random_disconnected_20.txt",
        4001
    )

    generate_random_disconnected(
        100,
        10,
        "mst_random_disconnected_100.txt",
        4002
    )

    print("\nAll MST test cases generated successfully.")


if __name__ == "__main__":
    main()
