function solution(s) {
  let seen = {};
  let answer = [];

  s.split("").forEach((item, idx) => {
    if (item in seen) {
      answer.push(idx - seen[item]);
    } else {
      answer.push(-1);
    }
    seen[item] = idx;
  });

  return answer;
}
