#!/usr/bin/node

// This script contains a square class

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    const charac = c === undefined ? 'X' : c;

    for (i = 0; i < this.height; i++) {
      console.log(charac.repeat(this.width));
    }
  }
};
