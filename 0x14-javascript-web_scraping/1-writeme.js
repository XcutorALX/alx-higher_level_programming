#!/usr/bin/node
// A script that reads and prints the content of a fileconst { readFile } = require('node:fs/promises');
const { writeFile } = require('node:fs/promises');
async function logFile (filePath, buffer) {
  try {
    await writeFile(filePath, buffer, 'utf8');
  } catch (err) {
    console.log(err);
  }
}

if (process.argv.length >= 4) {
  const myFile = process.argv[2];
  const data = process.argv[3];
  logFile(myFile, data);
}
