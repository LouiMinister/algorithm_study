# 좋은 구ㅏㄴ

L = int(input())
ary = list(map(int, input().split(" ")))
pivot = int(input())


# L 이 1이면 
 # -> pivot 이 그 원소이므로 return 0
if L == 1:
  print("0")
  exit() 

 
# pivot 보다 작으면서 가장 큰 값
pivot_min = 0
# pivot 보다 크면서 가장 작은 값
pivot_max = max(ary)

# pivot 하고 같은 값이 집합 안에 있으면 return 0
for v in ary:
  if v == pivot:
    print("0")
    exit()
    
  if v < pivot:
    pivot_min = max(pivot_min, v)
  if v > pivot:
    pivot_max = min(pivot_max, v)
    
# print(pivot_min, pivot_max)
res = (pivot - pivot_min) * (pivot_max - pivot) - 1
print(res)
