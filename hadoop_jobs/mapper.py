import sys

for line in sys.stdin:

    line = line.strip()

    fields = line.split(",")

    if fields[0] == "age":
        continue

    job = fields[1]

    balance = fields[5]

    print(
    f"{job}\t{balance}"
    )