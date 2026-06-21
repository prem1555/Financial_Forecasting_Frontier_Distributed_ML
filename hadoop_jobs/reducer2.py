import sys

counts={}

for line in sys.stdin:

    edu,housing=line.strip().split("\t")

    if housing=="yes":

        counts[edu]=counts.get(edu, 0)+1

for k,v in counts.items():

    print(k, v)