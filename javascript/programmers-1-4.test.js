/* eslint-disable no-undef */

const { describe, it } = require('node:test');
// eslint-disable-next-line camelcase
const solution1_4 = require('./programmers-1-4');

test('', () => {});

const context = describe;
describe('연속 숫자 제거 함수는', () => {
  context('arr = [1, 1, 3, 3, 0, 1, 1] 이면', () => {
    const arr = [1, 1, 3, 3, 0, 1, 1];
    it('길이 4의 배열을 return', () => {
      expect(solution1_4(arr)).toHaveLength(4);
    });
  });
  context('arr = [4, 4, 4, 3, 3] 이면', () => {
    const arr = [4, 4, 4, 3, 3];
    it('길이 2의 배열을 return', () => {
      expect(solution1_4(arr)).toHaveLength(2);
    });
  });
});
