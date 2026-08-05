#!/bin/bash
# Runs the gemm_driver on every test file and checks that
# Simple and Blocking produce identical result matrices.

DRIVER="./assignment_01/driver/gemm_driver"
TESTS="./assignment_01/tests"

for i in $(seq -w 1 25); do
    FILE="$TESTS/gemm_test_$i.txt"
    if [ ! -f "$FILE" ]; then
        continue
    fi

    OUTPUT=$("$DRIVER" "$FILE")

    # Extract just the two "Result matrix:" blocks (everything between
    # "Result matrix:" and "Execution time:") and compare them.
    SIMPLE=$(echo "$OUTPUT" | awk '/Algorithm: GEMM Simple/{flag=1;next}/Execution time/{flag=0}flag')
    BLOCKING=$(echo "$OUTPUT" | awk '/Algorithm: GEMM Blocking/{flag=1;next}/Execution time/{flag=0}flag')

    if [ "$SIMPLE" == "$BLOCKING" ]; then
        echo "Test $i: PASS"
    else
        echo "Test $i: FAIL  <-- mismatch!"
    fi
done
