#!/usr/bin/node

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

const filePath = resolve(process.argv.slice(2)[0]);
logFile(filePath);
