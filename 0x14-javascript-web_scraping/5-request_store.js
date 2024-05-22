#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');
const { writeFile } = require('node:fs/promises');

const myFile = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const data = body;
    logFile(myFile, data);
  }
});

async function logFile (filePath, buffer) {
  try {
    await writeFile(filePath, buffer, 'utf8');
  } catch (err) {
    console.log(err);
  }
}
