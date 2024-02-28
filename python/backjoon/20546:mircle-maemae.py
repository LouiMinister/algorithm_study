initCash = int(input())
stocks = list(map(int, input().split(' ')))

def lastStockPrice(cnt):
  return stocks[len(stocks)-1] * cnt

upOrDowns = [0]
for i, stock in enumerate(stocks[1:], start=1):
  if(stocks[i-1] < stock):
    upOrDowns.append(1)
  elif(stocks[i-1] > stock):
    upOrDowns.append(-1)
  else:
    upOrDowns.append(0)
  
# 3일 연속 상승한 날 -> 최대 매도
# 3일 연속 하락한 날 -> 전량 매수

contUpOrDowns = [0,0,0] # -1 전량매도, +1 전량매입
for i, upOrDown in enumerate(upOrDowns[3:], start=3):
  # print(i, upOrDown)
  if(upOrDowns[i-2] > 0 and upOrDowns[i-1] > 0 and upOrDowns[i] > 0):
    contUpOrDowns.append(-1)
  elif(upOrDowns[i-2] < 0 and upOrDowns[i-1] < 0 and upOrDowns[i] < 0):
    contUpOrDowns.append(1)
  else:
    contUpOrDowns.append(0)

    
junCash = initCash
junStocks = 0
sunCash = initCash
sunStocks = 0

# print(contUpOrDowns)

for i in range(len(stocks)):
  #준
  if (junCash >= stocks[i]):
    buyCnt = junCash // stocks[i]
    junCash -= buyCnt * stocks[i]
    junStocks += buyCnt
  
  #성
  if (contUpOrDowns[i] == 1):
    buyCnt = sunCash // stocks[i]
    sunCash -= buyCnt * stocks[i]
    sunStocks += buyCnt
  elif (contUpOrDowns[i] == -1):
    sunCash += sunStocks * stocks[i]
    sunStocks = 0
    
  # print(junCash, junStocks, sunCash, sunStocks)
    
lastStockPrice = stocks[len(stocks)-1]
junCash += junStocks * lastStockPrice
sunCash += sunStocks * lastStockPrice

if(junCash > sunCash):
  print("BNP")
elif(sunCash > junCash):
  print("TIMING")
else:
  print("SAMESAME")
