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

with open(os.path.join(OUT_DIR, "test_manifest.txt"), "w") as f:
    f.write("GEMM Test Case Manifest\n")
    f.write("=" * 50 + "\n")
    f.write("\n".join(manifest_lines) + "\n")

print("\nDone. See test_manifest.txt for the full list.")
