/**
 * [23.02.01 - Baekjoon] 1463 1로 만들기
 * @param {number} N 1 <= N <= 10^6 (정수)
 * @returns {number} 연산을 하는 횟수의 최솟값
 */
function makeOne(N) {
  d = Array(N + 1).fill(0);
  d[2] = d[3] = 1;

  for (let i = 4; i <= N; i++) {
    d[i] = d[i - 1] + 1;
    if (i % 3 === 0) {
      d[i] = Math.min(d[i / 3] + 1, d[i]);
    }
    if (i % 2 === 0) {
      d[i] = Math.min(d[i / 2] + 1, d[i]);
    }
  }
  return d[N];
}

console.log(makeOne(Number(N)));
