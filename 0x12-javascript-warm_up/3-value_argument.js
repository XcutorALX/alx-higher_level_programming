#!/usr/bin/node
const argLen = process.argv.length;
if (argLen == 2) {
  console.log("No argument");
} else {
  console.log(process.argv[2]);
}
