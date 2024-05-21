#!/usr/bin/node
// A script that reads and prints the content of a file

const { readFile } = require('node:fs/promises');
const { resolve } = require('node:path');

async function logFile (filePath) {
  try {
    const contents = await readFile(filePath, { encoding: 'utf8' });
    console.log(contents);
  } catch (err) {
    console.log(err);
  }
}

if (process.argv.length >= 3) {
  const myFile = resolve(process.argv[2]);
  logFile(myFile);
}
