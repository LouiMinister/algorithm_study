/*
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
*/

function solution(nums) {
  return sumOf(nums).map(isPrime).filter((bool) => bool).length;
}
console.log(solution([1, 2, 3, 4]));

function isPrime(num) {
  if (num <= 1) { return true; }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) { return false; }
  }
  return true;
}

function sumOf(ary) {
  const result = [];
  const len = ary.length;
  let [i, j, k] = [0, 0, 0];
  for (i; i < len - 2; i++) {
    j = i + 1;
    for (j; j < len - 1; j++) {
      k = j + 1;
      for (k; k < len; k++) {
        result.push(ary[i] + ary[j] + ary[k]);
      }
    }
  }
  return result;
}
