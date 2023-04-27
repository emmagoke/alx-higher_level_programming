#!/usr/bin/node
/**
 * This javascript script prints the number of movies where the
 * character “Wedge Antilles” is present.
 */
const request = require('request');
const apiUrl = process.argv[2];
let jsonBody;
let count = 0;
let i;
const characterId = '/18/';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    jsonBody = JSON.parse(body);
    for (i = 0; i < jsonBody.results.length; i++) {
      for (const character of jsonBody.results[i].characters) {
        /* array.incudes checks if an element is in an array */
        if (character.endsWith(characterId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
