# 럭키 스트레이트

str = input()
half = len(str)//2
num1 = list(map(int, str[:half]))
num2 = list(map(int, str[half:]))

if sum(num1) == sum(num2):
    print("LUCKY")
else:
    print("READY")

