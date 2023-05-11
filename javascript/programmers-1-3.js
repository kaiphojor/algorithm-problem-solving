function level1Number3(s) {
  const lenHalf = s.length / 2;
  return lenHalf === parseInt(lenHalf, 10) ? s.slice(lenHalf - 1, lenHalf + 1) : s[parseInt(lenHalf, 10)];
}

module.exports = level1Number3;
