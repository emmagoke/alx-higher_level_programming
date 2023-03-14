#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      /* if c is undefined */
      c = 'X';
    }
    let temp = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        temp += c;
      }
      if (i !== this.height - 1) {
        temp += '\n';
      }
    }
    console.log(temp);
  }
};
