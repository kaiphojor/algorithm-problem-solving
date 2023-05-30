/* eslint-disable no-undef */

const { describe, it } = require('node:test');
// eslint-disable-next-line camelcase
const solution1_5 = require('./programmers-1-5');

test('', () => {});

const context = describe;
describe('1-5 solution function', () => {
  context('when arr is [5, 9, 7, 10] and divisor is 5', () => {
    const arr = [5, 9, 7, 10];
    const divisor = 5;
    it('returns [5,10]', () => {
      expect(solution1_5(arr, divisor)).toEqual([5, 10]);
    });
  });
  context('when arr is [2, 36, 1, 3] and divisor is 1', () => {
    const arr = [2, 36, 1, 3];
    const divisor = 1;
    it('returns [1, 2, 3, 36]', () => {
      expect(solution1_5(arr, divisor)).toEqual([1, 2, 3, 36]);
    });
  });
  context('when arr is [3,2,6] and divisor is 10', () => {
    const arr = [3, 2, 6];
    const divisor = 10;
    it('returns [-1]', () => {
      expect(solution1_5(arr, divisor)).toEqual([-1]);
    });
  });
});
