n = int(input().strip())

student_marks = {}

for _ in range(n):
    line = input().strip().split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

query_name = input().strip()

query_scores = student_marks[query_name]

average = sum(query_scores) / len(query_scores)

print(f"{query_name} {average:.2f}")