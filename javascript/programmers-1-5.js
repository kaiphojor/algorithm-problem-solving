function level1Number5(arr, divisor) {
  const answer = arr.filter(item => item % divisor === 0).sort((a, b) => a - b);

  return answer.length > 0 ? answer : [-1];
}

module.exports = level1Number5;
