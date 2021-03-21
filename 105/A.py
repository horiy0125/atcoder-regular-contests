A, B, C, D = map(int, input().split())

result = False

for a in [True, False]:
    for b in [True, False]:
        for c in [True, False]:
            for d in [True, False]:
                eat = 0
                leave = A + B + C + D

                choice = [a, b, c, d]
                delicious = [A, B, C, D]

                for i in range(4):
                    if choice[i]:
                        eat += delicious[i]

                leave -= eat

                if leave == eat:
                    result = True
                    break

if result == True:
    print('Yes')
else:
    print('No')
