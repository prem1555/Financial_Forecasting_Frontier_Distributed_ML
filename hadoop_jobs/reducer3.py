import sys

counts={}

for line in sys.stdin:

    k,v=line.strip().split("\t")

    counts[k]=counts.get(
    k,
    0
    )+1

for k,v in counts.items():

    print(
    k,
    v
    )