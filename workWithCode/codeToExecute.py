

import sys

if len(sys.argv) != 2:
    print("Usage: python3 gen_add.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "w") as f:
    f.write("""
def add(a, b):
    return a + b

print(add(2, 3))
""")