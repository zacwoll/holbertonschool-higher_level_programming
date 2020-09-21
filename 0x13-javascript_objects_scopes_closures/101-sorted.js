#!/usr/bin/node
// Computes a dictionary of user ids by occurrence
const dict = require('./101-data').dict;
const sorted = (obj) => {
  const reversed = {};
  Object.keys(obj).forEach((key) => {
    reversed[obj[key]] = reversed[obj[key]] || [];
    reversed[obj[key]].push(key);
  });
  return reversed;
};
console.log(sorted(dict));
