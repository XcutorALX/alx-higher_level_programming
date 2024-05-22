#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');
const url = process.argv[2];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let i = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const result = JSON.parse(body).results;
    for (let j = 0; j < result.length; j++) {
      result[j].characters.includes(charUrl) && i++;
    }
    console.log(i);
  }
});
