##
# 문제 설명
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
#
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
#
# 제한 조건
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.
# 입출력 예
# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"
# 출처

def solution(number, k)
  targetIdx = 0
  numberAry = number.split('')
  def findMaxValueIdx(numberAry=[], targetIdx = 0, len = 0)
    numberAry[targetIdx, len+1].each_with_index.reduce([0,0]) do |acc, (v, i)|
      acc[0] >= v.to_i ? acc : [v.to_i, i]
    end[1] + targetIdx
    # max = [0,0]
    # (targetIdx..(targetIdx+len)).each do |i|
    #   max = max[0] >= numberAry[i].to_i ? max : [numberAry[i].to_i, i]
    #   break if max[0] == '9'
    # end
    # return max[1]
  end

  while k > 0 && targetIdx < numberAry.length
  # for i in (0..5)
    maxValIdx = findMaxValueIdx(numberAry, targetIdx, k)
    p [numberAry, k, targetIdx, maxValIdx]
    if maxValIdx == targetIdx then targetIdx +=1
    else
      numberAry.delete_if.with_index {|val, idx| targetIdx <= idx && idx < maxValIdx}
      k-= (maxValIdx - targetIdx)
    end
  end
  # numberAry.drop
  # 1. targetIdx 부터 k+1 개중 max값의 index 찾기
  #   1-1. max 값이 targetIdx 값이면 targetIdx +=1
  #   1-2  targetIdx 부터 maxValIdx 전까지 삭제, drop 한 만큼 k 에서 줄이기
  #
  # p numberAry
  #
  return numberAry[0..-(1+k)].join('')
end

puts solution("4177252841",	4)
#
# a = [0,1,2,3,4].each_with_index.reduce([0,0]) do |acc, (v, i)|
#   acc[0] > v ? acc : [v, i]
# end
#
# puts a
