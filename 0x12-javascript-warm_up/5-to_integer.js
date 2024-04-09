#!/usr/bin/node

// This script prints intergers passed as arguments

const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
