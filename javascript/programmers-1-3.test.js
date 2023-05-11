
const solution1_3 = require('./programmers-1-3');
const { describe, it } = require('node:test');

const context = describe;
describe('단어는', () => {
  context('홀수일 때', () => {
    it('가운데 글자 하나를 반환한다', () => {
      expect(solution1_3('abcde')).toBe('c');
    });
  });
  context('짝수일 때', () => {
    it('가운데 글자 두개를 반환한다', () => {
      expect(solution1_3('qwer')).toBe('we');
    });
  });
});
