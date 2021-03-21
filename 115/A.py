N, M = map(int, input().split())


def inversion_answer(answer: str):
    answer = answer.replace("1", ".")
    answer = answer.replace("0", "1")
    answer = answer.replace(".", "0")

    return answer


answers = []
count = 0

for _ in range(N):
    answer = input()
    answers.append(answer)

appear = set()
duplicates = []

for answer in answers:
    if answer in appear:
        duplicates.append(answer)
    else:
        appear.add(answer)
        appear.add(inversion_answer(answer))

print(2 ** M - len(duplicates))
