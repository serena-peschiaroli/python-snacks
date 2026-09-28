# Given the participants' scoresheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
from unittest import runner

n = int(input())

scores = list(map(int, input().split()))

unique_scores = set(scores)

unique_scores.remove(max(unique_scores))

runner_up = max(unique_scores)

print(runner_up)