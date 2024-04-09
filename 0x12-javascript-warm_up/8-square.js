#!/usr/bin/node

// This script prints intergers passed as arguments

const arg = process.argv[2];
let i;
let size = Number(arg);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
