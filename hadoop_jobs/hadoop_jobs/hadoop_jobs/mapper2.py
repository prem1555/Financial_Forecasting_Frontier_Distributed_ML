import sys

for line in sys.stdin:

    line=line.strip()

    fields=line.split(",")

    if fields[0]=="age":
        continue

    education=fields[3]

    housing=fields[6]

    print(f"{education}\t{housing}")
