import sys

current_job = None

total = 0

count = 0

for line in sys.stdin:

    job,balance = line.strip().split("\t")

    balance = float(balance)

    if current_job == job:

        total += balance

        count += 1

    else:

        if current_job:

            print(
            current_job,
            total/count
            )

        current_job = job

        total = balance

        count = 1

if current_job:

    print(
    current_job,
    total/count
    )