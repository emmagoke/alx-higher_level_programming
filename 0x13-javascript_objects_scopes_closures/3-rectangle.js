#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let temp = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        temp += 'X';
      }
      if (i !== this.height - 1) {
        temp += '\n';
      }
    }
    console.log(temp);
  }
};
