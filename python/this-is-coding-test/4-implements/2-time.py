# 시각

n = int(input())
cnt = 0
time_hour, time_min, time_sec = 0, 0, 0

for time_hour in range(n+1):
    for time_min in range(60):
        for time_sec in range(60):
            if '3' in str(time_hour)+str(time_min)+str(time_sec): cnt += 1

print(cnt)