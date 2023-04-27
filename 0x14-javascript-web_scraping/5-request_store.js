#!/usr/bin/node
/* This script  gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const fileName = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fileName, body, error => {
    if (error) {
      console.log(error);
    }
  });
});
