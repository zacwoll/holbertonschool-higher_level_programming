#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  const reverse = [];
  for (const item of list) {
    reverse.unshift(item);
  }
  return reverse;
};
