#!/usr/bin/node
/**
 * This script prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 */
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
let jsonBody;

request(apiUrl + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    /* JSON.parse converts a string to json */
    jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});
