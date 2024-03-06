# q [q]
# u [qu]
# q [qu], [q]
# a [qua], [q]
# c [quac], [q]
# u [quac], [qu]
# k [quack], [qu]
# q [qu], [q]
# a [qua], [q]
# u [qua], [qu]
# a [qua], [qua]
# c [quac], [qua]
# k [quack], [qua]
# c [quack], [qua]
# k [quack], [quak]

# ducks = [0, 0, 0, 0, 0]
# i값 들어오면 [i-1]--, [i]++ 

msgs = list(input())
nums = []
for char in msgs:
  if char == 'q':
    nums.append(0)
  elif char == 'u':
    nums.append(1)
  elif char == 'a':
    nums.append(2)
  elif char == 'c':
    nums.append(3)
  elif char == 'k':
    nums.append(4)

memo = [0 for _ in range(4)]

def proc():
  res = 0
  for num in nums:
    if num == 0:
      memo[0] += 1
    else:
      if memo[num-1] <= 0:
        return -1
      memo[num-1] -= 1
      if num < 4:
        memo[num] += 1
    res = max(res, sum(memo))
  if sum(memo) > 0: 
    return -1
  else:
    return res

print(proc())


