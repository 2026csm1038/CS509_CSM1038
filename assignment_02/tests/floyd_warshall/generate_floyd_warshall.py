import random
from pathlib import Path


OUTPUT_DIR = Path("assignment_02/tests/floyd_warshall")


def generate_graph(vertices, edge_probability, filename, seed):
    random.seed(seed)

    output_file = OUTPUT_DIR / filename

    with output_file.open("w") as file:
        file.write(f"{vertices}\n")

        for i in range(vertices):
            row = []

            for j in range(vertices):
                if i == j:
                    row.append("0")
                    continue

                if random.random() < edge_probability:
                    weight = random.randint(1, 20)

                    # Avoid negative self-cycles; self-loops are
                    # already excluded by i == j above.
                    row.append(str(weight))
                else:
                    row.append("INF")

            file.write(" ".join(row) + "\n")

    print(
        f"Generated {filename}: "
        f"V={vertices}"
    )


def generate_negative_cycle_test():
    vertices = 10

    matrix = [
        [0,    2,    "INF", 4,    "INF", "INF", "INF", "INF", "INF", "INF"],
        ["INF", 0,   -5,    "INF", 3,    "INF", "INF", "INF", "INF", "INF"],
        [1,    "INF", 0,    "INF", "INF", "INF", "INF", "INF", "INF", "INF"],
        ["INF", "INF", "INF", 0,    2,    "INF", "INF", "INF", "INF", "INF"],
        ["INF", "INF", "INF", "INF", 0,    1,    "INF", "INF", "INF", "INF"],
        ["INF", "INF", "INF", "INF", "INF", 0,    2,    "INF", "INF", "INF"],
        ["INF", "INF", "INF", "INF", "INF", "INF", 0,    3,    "INF", "INF"],
        ["INF", "INF", "INF", "INF", "INF", "INF", "INF", 0,    4,    "INF"],
        ["INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 0,    5],
        ["INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 0],
    ]

    output_file = OUTPUT_DIR / "fw_negative_cycle.txt"

    with output_file.open("w") as file:
        file.write(f"{vertices}\n")

        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")

    print("Generated fw_negative_cycle.txt")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Required Floyd-Warshall sizes:
    # 10, 100, 500, 1000, 2000
    #
    # The matrix is dense by definition, so every possible pair
    # is represented. INF means there is no direct edge.

    test_cases = [
        (10, 0.30, "fw_10.txt", 2001),
        (100, 0.10, "fw_100.txt", 2002),
        (500, 0.05, "fw_500.txt", 2003),
        (1000, 0.03, "fw_1000.txt", 2004),
        (2000, 0.02, "fw_2000.txt", 2005),
    ]

    for vertices, probability, filename, seed in test_cases:
        generate_graph(
            vertices,
            probability,
            filename,
            seed
        )

    generate_negative_cycle_test()


if __name__ == "__main__":
    main()
