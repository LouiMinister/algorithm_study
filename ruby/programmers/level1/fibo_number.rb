def solution(n)
  cache = [0, 1]
  def fibo(n)

    if !cache[n]
      cache[n] = fibo(n-1) + fibo(n-2)
    end
    return cache[n]
  end

  return fibo(n)
end
