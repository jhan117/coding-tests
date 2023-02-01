// 백준 제출용 코드
const N = require("fs").readFileSync("/dev/stdin").toString().trim();

/**
 * [23.01.31 - Baekjoon] 2839 설탕 배달
 * @param {number} N 배달할 설탕 무게
 * @returns {number} 가져가야 할 최소 봉지의 개수
 */
function sugar(N) {
  let fiveBag = parseInt(N / 5);
  let threeBag = N % 5;

  while (fiveBag >= 0) {
    if (threeBag % 3 === 0) return fiveBag + threeBag / 3;
    fiveBag -= 1;
    threeBag += 5;
  }
  return -1;
}

console.log(sugar(Number(N)));
