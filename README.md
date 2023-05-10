# algorithm-problem-solving

주로 javascript 알고리즘 문제를 푸는 repository

## 환경 설정(Javascript(Node) & VS-CODE & WSL & Jest)

1. Node 설치 : 직접 설치 or fnm(fast node manager) 통한 설치

2. Code Runner vs-code Extension 설치

3. [Code Runner 환경 설정](https://stackoverflow.com/questions/44983472/how-to-run-javascript-code-in-visual-studio-code-bin-sh-1-node-not-found)

```bash
which node
<Node 설치 경로>
```

`Ctrl + ,` (VS-CODE -> Preference -> Settings)

설정 창에서 Executor Map 검색 -> settings.json 에서 편집

해당 속성 settings.json에 추가

```json
"code-runner.executorMap": {
            "javascript": "<Node 설치 경로>"
}
```

code runner 실행은 `Ctrl + Alt + N` 으로 가능

4. jest 설치

```bash
# jest 설치
npm i -D jest
```

사용법

* `npx jest` : test code에 대한 test 수행
* `npx jest --watch` : 파일을 감시하다가 변경사항이 발생되면(저장시) test 수행

## 테스트 코드 작성법

Common JS 기준으로 작성한다

### 문제 함수부

`sum.js`

```javascript
function sum(a, b) {
  return a + b;
}
module.exports = sum; // 모듈 내보내기
```

### test 부분

`sum.test.js` 에 작성

#### 테스트(기본)

```javascript
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

### Describe - Context - It 패턴(BDD 스타일 중)

context는 describe를 활용해서 사용한다.

```javascript
const context = describe;

describe('무엇이',()=>{
  context('어떤 환경(상황)에서',()=>{
    it('어떻게 행동한다', ()=>{
      expect(solution1_1([3,1,2,3])).toBe(2);
    });
  });
});
```

## SOLVED (JS)

|**번호**|**제목**|**분류**|**코드**|**테스트**|
|:---:|:---:|:---:|:---:|:---:|
|2|2016년|구현|[코드](/javascript/programmers-1-2.js)|[테스트](/javascript/programmers-1-2.test.js)|
|1|폰켓몬|해시|[코드](/javascript/programmers-1-1.js)|[테스트](/javascript/programmers-1-1.test.js)|
