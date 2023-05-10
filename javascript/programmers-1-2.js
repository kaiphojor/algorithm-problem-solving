function solution1_2(a, b) {
  const dayOfMonth = [0,31,29,31,30,31,30,31,31,30,31,30,31];
  const dayOfWeek =  ['THU','FRI','SAT','SUN','MON','TUE','WED'];
  let days = dayOfMonth.slice(0,a).reduce((acc,cur)=>acc+cur,b);
  return dayOfWeek[days % 7];
}

module.exports = solution1_2;