#!/usr/bin/node

function secondLargestInteger(...args) {
  const integers = args.map(Number).filter(Number.isInteger); // Filter out non-integer arguments
  if (integers.length <= 1) {
    console.log(0);
  } else {
    const sortedIntegers = integers.sort((a, b) => b - a); // Sort integers in descending order
    console.log(sortedIntegers[1]);
  }
}

secondLargestInteger(...process.argv.slice(2));
