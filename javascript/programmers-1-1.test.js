/* eslint-disable camelcase */
/* eslint-disable no-undef */
const { describe, it } = require('node:test');
const solution1_1 = require('./programmers-1-1');

const context = describe;

describe('폰켓몬 함수는', () => {
  context('포켓못 수 4, 총 3종류 일때', () => {
    it('반절인 2마리까지 고를 수 있다', () => {
      expect(solution1_1([3, 1, 2, 3])).toBe(2);
    });
  });
});

test('폰켓몬 test 1', () => {
  expect(solution1_1([3, 1, 2, 3])).toBe(2);
});

test('폰켓몬 test 2', () => {
  expect(solution1_1([3, 3, 3, 2, 2, 4])).toBe(3);
});

test('폰켓몬 test 3', () => {
  expect(solution1_1([3, 3, 3, 2, 2, 2])).toBe(2);
});
