# 틱택토

# 불가능한 경우
# 3줄이 두개 이상 있는 경우
# 3줄이 없는데 9칸 안찬 경우
# . 제외 놓은 개수 -> 짝수인경우 각자 /2 씩, 홀수인경우 X가 하나 더 많이
# 

def cntStraight(board):
  cnt = {"O": 0 , "X": 0, ".": 0}
  for i in range(3):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2]: 
      cnt[board[i][0]] = cnt[board[i][0]] + 1
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
      cnt[board[0][i]] = cnt[board[0][i]] + 1
  
  if board[0][0] == board[1][1] and board[1][1] == board[2][2]: 
    cnt[board[0][0]] = cnt[board[0][0]] + 1
  if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    cnt[board[0][2]] = cnt[board[0][2]] + 1
  return cnt

def countPlay(board):
  res = {".": 0, "X": 0, "O": 0}
  for i in range(3):
    for j in range(3):
      res[board[i][j]] = res[board[i][j]] + 1
  return res

def isInvalidEmpty(board):
  dotCnt = countPlay(board)["."]
  straightCnt = cntStraight(board)
  if dotCnt > 0 and straightCnt["O"] == 0 and straightCnt["X"] == 0: return True
  return False
  
def isInvalidTurn(board):
  playCnt = countPlay(board)
  straightCnt = cntStraight(board)
  turnCnt = 9 - playCnt["."]
  oCnt = playCnt["O"]
  xCnt = playCnt["X"]
 
  # O가 승리했는데 턴이 짝수로 돌아간게 아니면 에러
  if (straightCnt["O"] > 0 and turnCnt % 2 != 0): return True
  # X가 승리 했는데 턴이 홀수로 돌아간게 아니면 에러
  if (straightCnt["X"] > 0 and turnCnt % 2 != 1): return True

  normalOCnt = turnCnt//2
  normalXCnt = turnCnt - normalOCnt
  if oCnt != normalOCnt or xCnt != normalXCnt: return True
  return False  

while(True):
  str = input()
  if str == "end": break
  
  board = [str[0:3], str[3:6], str[6:9]]
  straightCnt = cntStraight(board)
  straightInvalid = straightCnt["O"] * straightCnt["X"] != 0 
  # print(straightInvalid, isInvalidEmpty(board), isInvalidTurn(board))
  if straightInvalid or isInvalidEmpty(board) or isInvalidTurn(board):
    print("invalid")
  else:
    print("valid")
