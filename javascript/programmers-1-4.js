function level1Number4(arr) {
  const answer = [arr[0]];
  // 이전과 같지 않으면 추가
  arr.reduce((acc, cur) => {
    if (acc !== cur) {
      answer.push(cur);
    }

    return cur;
  });

  return answer;
}

module.exports = level1Number4;
