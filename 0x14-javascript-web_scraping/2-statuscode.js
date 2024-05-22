#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');

const url = process.argv[2];
request(url, function (response, body) {
  console.log(`code: ${response.statusCode}`);
});
