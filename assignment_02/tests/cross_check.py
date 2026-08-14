import subprocess
import sys
import tempfile
import os
import math


TOLERANCE = 1e-6


def read_matrix_file(filename):
    with open(filename, "r") as f:
        tokens = f.read().split()

    V = int(tokens[0])
    values = tokens[1:]

    if len(values) != V * V:
        raise ValueError(
            f"Expected {V * V} matrix values, found {len(values)}"
        )

    matrix = []
    index = 0

    for i in range(V):
        row = []

        for j in range(V):
            value = values[index]
            index += 1

            if value == "INF":
                row.append(None)
            else:
                row.append(float(value))

        matrix.append(row)

    return V, matrix


def create_bellman_input(matrix, source, filename):
    V = len(matrix)

    adjacency = [[] for _ in range(V)]
    edge_count = 0

    for u in range(V):
        for v in range(V):
            weight = matrix[u][v]

            if weight is None:
                continue

            # The diagonal zero represents distance to itself,
            # not an explicit self-loop.
            if u == v and weight == 0:
                continue

            adjacency[u].append((v, weight))
            edge_count += 1

    with open(filename, "w") as f:
        f.write(f"{V} {edge_count}\n")

        for u in range(V):
            f.write(f"{u} {len(adjacency[u])}")

            for v, weight in adjacency[u]:
                if weight.is_integer():
                    weight_text = str(int(weight))
                else:
                    weight_text = str(weight)

                f.write(f" {v} {weight_text}")

            f.write("\n")

        f.write(f"SOURCE {source}\n")


def run_floyd_warshall(filename):
    command = [
        "./assignment_02/driver/floyd_warshall_driver",
        filename
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            "Floyd-Warshall driver failed:\n" + result.stderr
        )

    output = result.stdout

    if "Negative weight cycle detected." in output:
        return None

    lines = output.splitlines()

    start = None

    for i, line in enumerate(lines):
        if line.strip() == "Shortest Distance Matrix:":
            start = i + 1
            break

    if start is None:
        raise RuntimeError(
            "Could not find Floyd-Warshall distance matrix."
        )

    matrix = []

    for line in lines[start:]:
        line = line.strip()

        if not line:
            break

        if line.startswith("Execution"):
            break

        row = []

        for value in line.split():
            if value == "INF":
                row.append(None)
            else:
                row.append(float(value))

        matrix.append(row)

    return matrix


def run_bellman_ford(filename):
    command = [
        "./assignment_02/driver/bellman_ford_driver",
        filename
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            "Bellman-Ford driver failed:\n" + result.stderr
        )

    output = result.stdout

    if "Negative cycle: Yes" in output:
        return None

    distances = {}

    reading = False

    for line in output.splitlines():

        if line.strip() == "Vertex Distance":
            reading = True
            continue

        if not reading:
            continue

        if line.startswith("Negative cycle:"):
            break

        parts = line.split()

        if len(parts) != 2:
            continue

        vertex = int(parts[0])

        if parts[1] == "INF":
            distances[vertex] = None
        else:
            distances[vertex] = float(parts[1])

    return distances


def compare(source, floyd_row, bellman_distances):
    V = len(floyd_row)

    for v in range(V):

        expected = floyd_row[v]
        actual = bellman_distances.get(v)

        if expected is None and actual is None:
            continue

        if expected is None or actual is None:
            return False, v, expected, actual

        if abs(expected - actual) > TOLERANCE:
            return False, v, expected, actual

    return True, None, None, None


def cross_check(filename):

    print("=" * 65)
    print("Bellman-Ford / Floyd-Warshall Cross-Check")
    print("=" * 65)
    print(f"Test file: {filename}")

    V, original_matrix = read_matrix_file(filename)

    print(f"Vertices: {V}")
    print(f"Bellman-Ford runs: {V}")
    print()

    # First run Floyd-Warshall on the ORIGINAL graph.
    floyd_result = run_floyd_warshall(filename)

    if floyd_result is None:
        print("Floyd-Warshall detected a negative cycle.")
        print()
        print("Cross-check cannot be performed because")
        print("shortest-path distances are undefined.")
        return False

    if len(floyd_result) != V:
        raise RuntimeError(
            f"Floyd-Warshall returned {len(floyd_result)} rows "
            f"instead of {V}."
        )

    mismatches = 0

    with tempfile.TemporaryDirectory() as temp_dir:

        for source in range(V):

            bf_input = os.path.join(
                temp_dir,
                f"bf_source_{source}.txt"
            )

            # Build BF input from the ORIGINAL graph.
            create_bellman_input(
                original_matrix,
                source,
                bf_input
            )

            bellman_result = run_bellman_ford(
                bf_input
            )

            if bellman_result is None:
                print(
                    f"Source {source:3d}: "
                    "FAIL (Bellman-Ford detected negative cycle)"
                )
                mismatches += 1
                continue

            passed, vertex, expected, actual = compare(
                source,
                floyd_result[source],
                bellman_result
            )

            if passed:
                print(
                    f"Source {source:3d}: PASS"
                )
            else:
                print(
                    f"Source {source:3d}: FAIL "
                    f"(vertex {vertex}: "
                    f"Floyd-Warshall={expected}, "
                    f"Bellman-Ford={actual})"
                )

                mismatches += 1

    print()
    print(f"Sources checked: {V}")
    print(f"Mismatches: {mismatches}")

    if mismatches == 0:
        print("Status: PASS")
        return True

    print("Status: FAIL")
    return False


def main():

    if len(sys.argv) != 2:
        print(
            "Usage: python3 assignment_02/tests/cross_check.py "
            "<floyd_warshall_test_file>"
        )
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Error: File not found: {filename}")
        sys.exit(1)

    try:
        passed = cross_check(filename)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
