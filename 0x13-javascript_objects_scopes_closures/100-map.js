#!/usr/bin/node
// Computers new array from imported array
const list = require('./100-data').list;
console.log(list);
const map = list.map((x, i) => x * i);
console.log(map);
