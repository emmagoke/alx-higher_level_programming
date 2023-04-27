#!/usr/bin/node
/* This script computes the number of tasks completed by user id. */

const request = require('request');

const apiUrl = process.argv[2];
const count = {};
let jsonBody;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    jsonBody = JSON.parse(body);
    for (const task of jsonBody) {
      if (task.completed) {
        count[`${task.userId}`] = count[`${task.userId}`] || 0;
        count[`${task.userId}`]++;
      }
    }
  }
  console.log(count);
});
