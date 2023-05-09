
function solution1_1(nums) {
  const setSize = new Set(nums).size;
  const halfSize = nums.length / 2;
  return setSize > halfSize ? halfSize : setSize;
}

module.exports = solution1_1;