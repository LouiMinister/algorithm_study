# 회의실 배정

N = int(input())
conferences = []
for _ in range(N):
  conferences.append(list(map(int, input().split(" "))))
  
conferences.sort(key = lambda x: (x[1], x[0]))

# print(conferences)

conferenceCnt = 0
prevConferenceEndTime = 0
for startTime, endTime in conferences:
  if startTime >= prevConferenceEndTime:
    conferenceCnt += 1
    prevConferenceEndTime = endTime

print(conferenceCnt)
