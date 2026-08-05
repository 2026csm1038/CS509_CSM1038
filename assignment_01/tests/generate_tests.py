import random
import os

random.seed(42)
OUT_DIR = os.path.dirname(__file__)

# (M, K, N, description)
CASES = [
    (0,   3,   3,   "Edge case: M=0 (empty A)"),
    (3,   0,   3,   "Edge case: K=0 (zero inner dimension)"),
    (1,   1,   1,   "Smallest non-trivial case"),
    (2,   3,   2,   "PDF example (fixed values)"),
    (5,   5,   5,   "Small square"),
    (10,  10,  10,  "Small square"),
    (3,   7,   2,   "Rectangular / non-square"),
    (8,   2,   9,   "Rectangular / non-square"),
    (8,   8,   8,   "Exactly at block boundary"),
    (64,  64,  64,  "Exactly at block boundary"),
    (63,  63,  63,  "Just below block boundary (uneven blocks)"),
    (65,  65,  65,  "Just above block boundary (uneven blocks)"),
    (100, 100, 100, "Medium"),
    (300, 300, 300, "Large"),
    (500, 500, 500, "Very large"),
]

manifest_lines = []

# --- Original 15 cases (unchanged) ---
for idx, (M, K, N, desc) in enumerate(CASES, start=1):
    fname = f"gemm_test_{idx:02d}.txt"
    path = os.path.join(OUT_DIR, fname)
    with open(path, "w") as f:
        f.write(f"{M} {K} {N}\n")
        if M == 2 and K == 3 and N == 2:
            # Fixed PDF example values, not random
            f.write("1 2 3\n4 5 6\n7 8\n9 10\n11 12\n")
        else:
            for _ in range(M):
                f.write(" ".join(str(random.randint(1, 10)) for _ in range(K)) + "\n")
            for _ in range(K):
                f.write(" ".join(str(random.randint(1, 10)) for _ in range(N)) + "\n")
    manifest_lines.append(f"{fname}: M={M}, K={K}, N={N} -- {desc}")
    print(f"Created {fname}: {M}x{K}x{N} -- {desc}")


# --- Helper for the new, more varied cases (16-24) ---
def write_random_test(idx, M, K, N, low=1, high=10, allow_negative=False, decimals=False, desc=""):
    fname = f"gemm_test_{idx:02d}.txt"
    path = os.path.join(OUT_DIR, fname)

    def val():
        v = round(random.uniform(low, high), 2) if decimals else random.randint(low, high)
        if allow_negative and random.random() < 0.5:
            v = -v
        return v

    with open(path, "w") as f:
        f.write(f"{M} {K} {N}\n")
        for _ in range(M):
            f.write(" ".join(str(val()) for _ in range(K)) + "\n")
        for _ in range(K):
            f.write(" ".join(str(val()) for _ in range(N)) + "\n")

    manifest_lines.append(f"{fname}: M={M}, K={K}, N={N} -- {desc}")
    print(f"Created {fname}: {M}x{K}x{N} -- {desc}")


# --- Helper for the identity-matrix case (25) ---
def write_identity_test(idx, N, desc=""):
    fname = f"gemm_test_{idx:02d}.txt"
    path = os.path.join(OUT_DIR, fname)
    A = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]

    with open(path, "w") as f:
        f.write(f"{N} {N} {N}\n")
        for row in A:
            f.write(" ".join(map(str, row)) + "\n")
        for i in range(N):
            row = [1 if j == i else 0 for j in range(N)]
            f.write(" ".join(map(str, row)) + "\n")

    manifest_lines.append(f"{fname}: M={N}, K={N}, N={N} -- {desc}")
    print(f"Created {fname}: {N}x{N}x{N} -- {desc}")


# --- New exhaustive additions (16-25) ---
write_random_test(16, 1, 6, 5, desc="Row vector x matrix (M=1)")
write_random_test(17, 5, 6, 1, desc="Matrix x column vector (N=1)")
write_random_test(18, 4, 1, 4, desc="K=1 (outer product style)")
write_random_test(19, 6, 6, 6, allow_negative=True, desc="Negative values included")
write_random_test(20, 5, 5, 5, decimals=True, low=-5, high=5, desc="Decimal / floating-point values")
write_random_test(21, 200, 4, 4, desc="Very tall and thin matrix")
write_random_test(22, 4, 4, 200, desc="Very short and wide matrix")
write_random_test(23, 6, 300, 6, desc="Large inner dimension only (stresses K-loop)")
write_random_test(24, 97, 89, 101, desc="Prime-ish dimensions (max uneven-block stress)")
write_identity_test(25, 6, desc="Identity multiplication (result must equal A exactly)")

with open(os.path.join(OUT_DIR, "test_manifest.txt"), "w") as f:
    f.write("GEMM Test Case Manifest\n")
    f.write("=" * 50 + "\n")
    f.write("\n".join(manifest_lines) + "\n")

print("\nDone. See test_manifest.txt for the full list.")
