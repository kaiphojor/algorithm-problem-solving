const {describe, it } = require('node:test');
const solution1_2 = require('./programmers-1-2');

const context = describe;

test('',()=>{});

describe('2016 year 함수는',()=>{
  context('a가 월, b가 일자 일때',()=>{

    it('5월 24일을 입력하면 TUE(화요일)이 반환된다.',()=>{
      expect(solution1_2(5,24)).toBe('TUE');
    });

    it('1월 1일을 입력하면 FRI(금요일)이 반환된다.',()=>{
      expect(solution1_2(1,1)).toBe('FRI');
    });

  });
});