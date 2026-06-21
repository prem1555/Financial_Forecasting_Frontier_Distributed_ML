import sys

for line in sys.stdin:

    line=line.strip()

    fields=line.split(",")

    if fields[0]=="age":
        continue

    month=fields[10]

    y=fields[16]

    print(
    f"{month}_{y}\t1"
    )