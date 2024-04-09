#!/usr/bin/node

// This script prints intergers passed as arguments

const arg = process.argv[2];
let i = Number(arg);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
