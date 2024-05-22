#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log(JSON.parse(body).title);
});
