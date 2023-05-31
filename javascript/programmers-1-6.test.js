/* eslint-disable no-undef */

const { describe, it } = require('node:test');
// eslint-disable-next-line camelcase
const solution1_6 = require('./programmers-1-6');

test('', () => {});

const context = describe;
describe('1-6 solution function', () => {
  context('when arr is ["sun", "bed", "car"] and n is 1', () => {
    const arr = ['sun', 'bed', 'car'];
    const n = 1;
    it('returns ["car", "bed", "sun"]', () => {
      expect(solution1_6(arr, n)).toEqual(['car', 'bed', 'sun']);
    });
  });
  context('when arr is ["abce", "abcd", "cdx"] and n is 2', () => {
    const arr = ['abce', 'abcd', 'cdx'];
    const n = 2;
    it('returns ["abcd", "abce", "cdx"]', () => {
      expect(solution1_6(arr, n)).toEqual(['abcd', 'abce', 'cdx']);
    });
  });
});
