megabytes = int(input())
months = int(input())
total_used = 0
total = 0

for i in range(months):
    total_used += int(input())

total = (megabytes * (months + 1)) - total_used

print(total)