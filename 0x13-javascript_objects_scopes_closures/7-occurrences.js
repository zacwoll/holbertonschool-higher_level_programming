#!/usr/bin/node
// Returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  for (const item of list) {
    if (item === searchElement) {
      number++;
    }
  }
  return number;
};
