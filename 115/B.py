import sys

N = int(input())

rows = []
for _ in range(N):
    rows.append(list(map(int, input().split())))


def calculate_differences(row):
    differences = []
    present_number = None
    for number in row:
        if present_number == None:
            present_number = number
        else:
            differences.append(number - present_number)

    return differences


standard_differences = calculate_differences(rows[0])
exist = True

for row in rows:
    differences = calculate_differences(row)
    if differences != standard_differences:
        exist = False
        break

columns = []

for n in range(N):
    column = []
    for row in rows:
        column.append(row[n])

    columns.append(column)

standard_differences = calculate_differences(columns[0])

for column in columns:
    differences = calculate_differences(column)
    if differences != standard_differences:
        exist = False
        break

if not exist:
    print('No')
    sys.exit()

A = rows[0]

initial = 0
B = [0]

for diff in standard_differences:
    B.append(initial + diff)

A_minimum_number = min(A)
B_minimum_number = min(B)

if A_minimum_number < B_minimum_number:
    for i in range(N):
        A[i] -= A_minimum_number
        B[i] += A_minimum_number
else:
    for i in range(N):
        A[i] += B_minimum_number
        B[i] -= B_minimum_number

print('Yes')
print(*B)
print(*A)


# A&B miss!!!
