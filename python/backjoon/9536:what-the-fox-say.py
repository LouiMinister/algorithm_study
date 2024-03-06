T = int(input())

for _ in range(T):
  says = input().split(' ')
  animalSays = set()
  while(True):
    animalSay = input().split(' ')
    if(animalSay[1]) == "does": break
    else:
      animalSays.add(animalSay[2])
  
  foxSays = []
  for say in says:
    if not say in animalSays:
      foxSays.append(say)
  print(' '.join(foxSays))
  