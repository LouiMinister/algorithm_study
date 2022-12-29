def solution(n)
  $cache = [0, 1]

  for i in 2..n
    $cache[i] = (($cache[i-1]) + ($cache[i-2])) % 1234567
  end
  $cache[n]
end
puts solution 100
