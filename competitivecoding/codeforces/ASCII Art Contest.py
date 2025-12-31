score = list(map(int, input().split()))
Max = max(score)
Min = min(score)
if Max - Min >= 10:
    print("check again")
else:
    score.sort()
    print("final",score[1])