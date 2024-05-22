#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

const out = {};
let key;
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const result = JSON.parse(body);
    for (let i = 0; i < result.length; i++) {
      key = result[i].userId;

      if (result[i].completed) {
        out[key] = key in out ? out[key] + 1 : 1;
      }
    }
    console.log(out);
  }
});
