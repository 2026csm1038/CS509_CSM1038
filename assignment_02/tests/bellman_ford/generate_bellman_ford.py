import random
from pathlib import Path


OUTPUT_DIR = Path("assignment_02/tests/bellman_ford")


def generate_graph(vertices, edges, filename, seed):
    random.seed(seed)

    output_file = OUTPUT_DIR / filename

    # We generate a sparse directed graph without storing
    # all possible edges in memory.
    #
    # To avoid accidental negative cycles, normal test graphs
    # use edges from lower-numbered vertices to higher-numbered
    # vertices.

    adjacency = [[] for _ in range(vertices)]

    # First create a simple chain so that all vertices except
    # the last have at least one outgoing edge.
    #
    # This also makes every vertex reachable from SOURCE 0.
    for u in range(vertices - 1):
        weight = random.randint(-10, 20)
        adjacency[u].append((u + 1, weight))

    remaining_edges = edges - (vertices - 1)

    used_edges = set()

    for u in range(vertices - 1):
        used_edges.add((u, u + 1))

    while remaining_edges > 0:
        u = random.randrange(0, vertices - 1)
        v = random.randrange(u + 1, vertices)

        if (u, v) in used_edges:
            continue

        used_edges.add((u, v))

        weight = random.randint(-10, 20)
        adjacency[u].append((v, weight))

        remaining_edges -= 1

    for neighbors in adjacency:
        neighbors.sort()

    with output_file.open("w") as file:
        file.write(f"{vertices} {edges}\n")

        for u in range(vertices):
            file.write(f"{u} {len(adjacency[u])}")

            for v, weight in adjacency[u]:
                file.write(f" {v} {weight}")

            file.write("\n")

        file.write("SOURCE 0\n")

    print(
        f"Generated {filename}: "
        f"V={vertices}, E={edges}"
    )


def generate_negative_cycle_test():
    vertices = 10

    adjacency = [
        [(1, 2), (3, 4)],
        [(2, -5), (4, 3)],
        [(0, 1)],
        [(5, 2)],
        [(6, 1)],
        [(7, 2)],
        [(8, 3)],
        [(9, 4)],
        [],
        []
    ]

    edges = sum(len(neighbors) for neighbors in adjacency)

    output_file = OUTPUT_DIR / "bf_negative_cycle.txt"

    with output_file.open("w") as file:
        file.write(f"{vertices} {edges}\n")

        for u in range(vertices):
            file.write(f"{u} {len(adjacency[u])}")

            for v, weight in adjacency[u]:
                file.write(f" {v} {weight}")

            file.write("\n")

        file.write("SOURCE 0\n")

    print("Generated bf_negative_cycle.txt")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    test_cases = [
        (10, 20, "bf_10.txt", 1001),
        (100, 300, "bf_100.txt", 1002),
        (10_000, 30_000, "bf_10000.txt", 1003),
        (50_000, 150_000, "bf_50000.txt", 1004),
        (100_000, 300_000, "bf_100000.txt", 1005),
    ]

    for vertices, edges, filename, seed in test_cases:
        generate_graph(
            vertices,
            edges,
            filename,
            seed
        )

    generate_negative_cycle_test()


if __name__ == "__main__":
    main()
