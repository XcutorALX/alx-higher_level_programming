#!/usr/bin/node

// This script contains a square class

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
