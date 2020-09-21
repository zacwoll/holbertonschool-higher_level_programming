#!/usr/bin/node
// Define a square
const oldSquare = require('./5-square');

class Square extends oldSquare {}

Square.prototype.charPrint = function (c) {
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
