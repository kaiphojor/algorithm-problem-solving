function level1Number6(strings, n) {
  strings.sort((a, b) => a[n] === b[n] ? a.localeCompare(b) : (a[n]).localeCompare(b[n]));
  return strings;
}

module.exports = level1Number6;
